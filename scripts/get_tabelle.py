from lxml import html
import requests
import re
import os
import sys
import json
import codecs
import create_sphinx_tables

class Anpr(object):
    @staticmethod
    def domain():
        return "https://www.anpr.interno.it"


class Table(object):
    def __init__(self,id, url, source,title, date, note):
        self.id = id
        self.url = url
        self.source = source
        self.title = title
        self.date = date
        self.note = note
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


def crawlXlsFromPath(xlsxpath,rstpath,url,section_prefix):
    page = requests.get(Anpr.domain()+url)
    print ("Get all Excel files from " +Anpr.domain()+url)
    tree = html.fromstring(page.content)

    xpath_expr = "//tr[td//text()[contains(., '.xlsx')]]"

    xpath_expr = "//tr[td//a[contains(@href,'.xlsx')]]"
    allTrWithTh = tree.xpath(xpath_expr)
    files_array =[]
    for tr in allTrWithTh:
        tds = tr.getchildren()
        xls_url = Anpr.domain()+ tds[1].getchildren()[0].get("href")
        title = tds[1].getchildren()[0].text
        print xls_url
        files_array.append(Table(tds[0].text,xls_url,tds[2].text,title,tds[3].text,tds[4].text))

    toclist = []
    for data in files_array:
        if data.title is None:
            print "FIXME: data.title is None in file:", data.url
            continue

        xlsx_name, rst_name = wGetAndRename(xlsxpath,rstpath,data.url,data.title,"tab")
        if xlsx_name == "":
            continue

        f = codecs.open(rst_name, "w", "utf-8")

        tablename = "Tabella %s - %s" % (data.id, data.title)
        print >>f, tablename
        print >>f, "="*len(tablename)
        print >>f
        if data.date.strip():
            print >>f, ":Aggiornamento: %s" % data.date
        if data.source.strip():
            print >>f, ":Fonte: %s" % data.source
        if data.note.strip():
            print >>f, ":Note: %s" % data.note
        print >>f

        create_sphinx_tables.convertXlsxToRst(xlsx_name, f)
        f.close()

        toclist.append((data.id, os.path.splitext(os.path.basename(rst_name))[0]))

    # generate toc
    f = open(rstpath + "/toc.rst", "w")
    print >>f, ".. toctree::"
    print >>f, "    :maxdepth: 2"
    print >>f, "    :caption: Contents"
    print >>f

    toclist.sort()
    for id,name in toclist:
        print >>f, "    %s" % name
    f.close()


def wGetAndRename(xlsxpath,rstpath,url,title,section_prefix):
    print "File to download " +url
    try:
        r = requests.get(url ,stream=True)
        r.raise_for_status()
    except requests.ConnectionError:
        print "ERROR: downloading file, skipping"
        return "", ""

    file_content = r.raw.read()
    print "Downloading: [" + url+ "]"
    print "Title:", title
    base_name = section_prefix+"_"+ re.sub(r'([^.a-zA-Z0-9_])','_',title)
    xlsx_name = xlsxpath + "/" + base_name + ".xlsx"
    rst_name = rstpath + "/" + base_name + ".rst"
    with open(xlsx_name, 'w') as f:
        f.write(file_content)
    return xlsx_name, rst_name



if __name__ == "__main__":
    #Downloads single contents
    #wGetAndRename("portale/documents/20182/26001/errori_anpr_20170301.xlsx/1e54c0fd-b77b-4980-9374-af6f05111578","Errori ANPR","error")
    #wGetAndRename("portale/documents/20182/26001/Allegato+9+-+Esiti+AE.xlsx/05d05160-20e5-4afc-9ba9-07fde16c8044","Errori Agenzia Entrate","error")

    if len(sys.argv) < 3:
        print "use get_tabelle.py [xlsx-path] [rst-path]"
        sys.exit(2)

    crawlXlsFromPath(sys.argv[1], sys.argv[2], "/portale/tabelle-di-riferimento","tab")

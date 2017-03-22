from lxml import html
import requests
import re
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


    # print files_array
    # with open('data.json', 'w') as outfile:
    #     json.dump(files_array, outfile)

    for data in files_array:
        xlsx_name, rst_name = wGetAndRename(xlsxpath,rstpath,data.url,data.title,"tab")

        f = codecs.open(rst_name, "w", "utf-8")

        tablename = "Tabella %s - %s" % (data.id, data.title)
        print >>f, tablename
        print >>f, "="*len(tablename)
        print >>f
        if data.date:
            print >>f, ":Aggiornamento: %s" % data.date
        if data.source:
            print >>f, ":Fonte: %s" % data.source
        if data.note:
            print >>f, ":Note: %s" % data.note
        print >>f

        create_sphinx_tables.convertXlsxToRst(xlsx_name, f)
        f.close()

'''
    allxlxs= tree.xpath("//a[contains(@href,'.xlsx')]")
    for xls in allxlxs:
        print xls
        if xls.text is not None:
            wGetAndRename(xls.get("href"),xls.text,section_prefix)
'''

def wGetAndRename(xlsxpath,rstpath,url,title,section_prefix):
    print "File to download " +url
    r = requests.get(url ,stream=True)
    print r.status_code
    if r.status_code == 200:
        file_content = r.raw.read()
        print "Downloading: [" + url+ "]"
        try:
            print title
            base_name = section_prefix+"_"+ re.sub(r'([^.a-zA-Z0-9_])','_',title)
            xlsx_name = xlsxpath + "/" + base_name + ".xlsx"
            rst_name = rstpath + "/" + base_name + ".rst"
            with open(xlsx_name, 'w') as f:
                f.write(file_content)
            return xlsx_name, rst_name
        except TypeError as detail:
            print "Unexpected error:", detail



if __name__ == "__main__":
    #Downloads single contents
    #wGetAndRename("portale/documents/20182/26001/errori_anpr_20170301.xlsx/1e54c0fd-b77b-4980-9374-af6f05111578","Errori ANPR","error")
    #wGetAndRename("portale/documents/20182/26001/Allegato+9+-+Esiti+AE.xlsx/05d05160-20e5-4afc-9ba9-07fde16c8044","Errori Agenzia Entrate","error")

    if len(sys.argv) < 3:
        print "use get_tabelle.py [xlsx-path] [rst-path]"
        sys.exit(2)

    crawlXlsFromPath(sys.argv[1], sys.argv[2], "/portale/tabelle-di-riferimento","tab")

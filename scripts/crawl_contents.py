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
    def __init__(self,id, url, source="", title="", date="", note=""):
        self.id = id
        self.url = url
        self.source = source
        self.title = title
        self.date = date
        self.note = note
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


def scrapeHtml(xlsxpath,rstpath,url,section_prefix):
    page = requests.get(Anpr.domain()+url)
    print ("Get all Excel files from " +Anpr.domain()+url)
    tree = html.fromstring(page.content)

    xpath_expr = "//tr[td//a[contains(@href,'.xlsx')]]"
    allTrWithTh = tree.xpath(xpath_expr)
    files_array =[]
    for tr in allTrWithTh:
        tds = tr.getchildren()
        href_url = tds[1].getchildren()[0].get("href")
        xls_url = href_url
        if(Anpr.domain() not in href_url):
            xls_url = Anpr.domain()+ href_url

        title = tds[1].getchildren()[0].text

        files_array.append(Table(tds[0].text,xls_url,tds[2].text,title,tds[3].text,tds[4].text))

    toclist = []
    for data in files_array:
        if data.title is None:
            print "FIXME: data.title is None in file:", data.url
            continue
        tocitem = createRstFromXlsx(data)
        if tocitem is not None:
            toclist.append(tocitem)

    return toclist


def createRstFromXlsx(data, table=True, startFromRow=0, nCols=2):
    xlsx_name, rst_name = wGetAndRename(xlsxpath,rstpath,data.url,data.title,"tab")
    if xlsx_name == "":
        return

    f = codecs.open(rst_name, "w", "utf-8")
    tablename = "%s" % (data.title)
    if table:
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
    print >>f, "`Download <%s>`_" % data.url
    print >>f
    print os.path.getsize(xlsx_name);
    if (os.path.getsize(xlsx_name)<1000000):
        create_sphinx_tables.convertXlsxToRst(xlsx_name, f, startFromRow, nCols)
    f.close()

    return (data.id, os.path.splitext(os.path.basename(rst_name))[0])



def createtoc(rstpath, toclist):
    # generate toc
    f = open(rstpath + "/toc.rst", "w")
    print >>f, ".. toctree::"
    print >>f, "    :maxdepth: 2"
    print >>f, "    :caption: Contenuti"
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
    base_name = base_name.lower()
    xlsx_name = xlsxpath + "/" + base_name + ".xlsx"
    rst_name = rstpath + "/" + base_name + ".rst"
    with open(xlsx_name, 'w') as f:
        f.write(file_content)
    return xlsx_name, rst_name



if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "use get_tabelle.py [xlsx-path] [rst-path]"
        sys.exit(2)

    xlsxpath = sys.argv[1]
    rstpath = sys.argv[2]
    toclist = []


    toclist = scrapeHtml(xlsxpath, rstpath, "/portale/tabelle-di-riferimento","tab")
    '''
    toclist.append(createRstFromXlsx(Table(
        id=0, url=Anpr.domain()+"/portale/documents/20182/26001/Utilizzo+WS+ANPR+27072016.xlsx",
        title="Utilizzo del WebService", date="1 Marzo 2017",
    ),False,4,3))

    '''




    toclist.append(createRstFromXlsx(Table(
        id=0, url=Anpr.domain()+"/portale/documents/20182/26001/aggiornamenti_29_03_2017.xlsx/910657e9-bc87-4f5b-9b2b-2d370d6d826f",
        title="Aggiornamenti alla documentazione tecnica", date="29 Marzo 2017",
    ),False))


    toclist.append(createRstFromXlsx(Table(
        id=0, url=Anpr.domain()+"/portale/documents/20182/26001/Allegato+5+-+Elenco+WS+di+ANPR+13102016.xlsx/a787b18d-a271-482c-bbb4-c3559d2b93c0",
        title="Elenco dei web services disponibili", date="17 dicembre 2017",
    ),False))

    toclist.append(createRstFromXlsx(Table(
        id=3, url=Anpr.domain()+"/portale/documents/20182/26001/Allegato+2+-+Elenco+funzioni+WEB2772016.xlsx",
        title="Elenco delle funzionalita' disponibili", date="17 Marzo 2017",
    ),False,0,3))


    toclist.append(createRstFromXlsx(Table(
        id=0, url=Anpr.domain()+"/portale/documents/20182/26001/errori_anpr_20170301.xlsx/1e54c0fd-b77b-4980-9374-af6f05111578",
        title="Elenco Errori ANPR", date="27 Aprile 2017",
    ),False))
    toclist.append(createRstFromXlsx(Table(
        id=1, url=Anpr.domain()+"/portale/documents/20182/26001/Allegato+9+-+Esiti+AE.xlsx/05d05160-20e5-4afc-9ba9-07fde16c8044",
        title="Errori Agenzia Entrate", date="27 Aprile 2017",
    ),False))

    toclist.append(createRstFromXlsx(Table(
        id=4, url=Anpr.domain()+"/portale/documents/20182/26001/tabella+3+archivio+comuni+20170413/43d8e1f4-bb22-4aaa-a74a-1e83c334dc6b",
        title="Tabella 03 - Comuni", source="Istat-Agenzia delle Entrate-Ministero dell'Interno", date="13 Aprile 2017",note="Variazioni dovute a operazioni di fusione e/o accorpamento di comuni"
    ),False))

    createtoc("../src/", toclist)

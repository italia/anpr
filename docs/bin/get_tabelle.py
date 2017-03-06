from lxml import html
import requests
import re
import sys
class Anpr(object):
    @staticmethod
    def domain():
        return "https://www.anpr.interno.it/"

def crawlXlsFromPath(url,section_prefix):
    page = requests.get(Anpr.domain()+url)
    print ("Get all xlsx from " +Anpr.domain()+url)
    tree = html.fromstring(page.content)

    allxlxs= tree.xpath("//a[contains(@href,'.xlsx')]")
    for xls in allxlxs:
        wGetAndRename(xls.get("href"),xls.text,section_prefix)


def wGetAndRename(path,title,section_prefix):
    r = requests.get(Anpr.domain()+path ,stream=True)
    print Anpr.domain()+path
    if r.status_code == 200:
        file_content = r.raw.read()
        print "Anpr Domain: "+Anpr.domain()
        #print "Downloading: [" + Anpr.domain()+path+"] "+title
        try:
            print title
            file_name= section_prefix+"_"+(re.sub(r'([^.a-zA-Z0-9_])','_',title) +".xlsx")
            file_location= "xlsx/"+file_name
            with open(file_location, 'w') as f:
                f.write(file_content)
        except TypeError as detail:
            print "Unexpected error:", detail



if __name__ == "__main__":

    crawlXlsFromPath("portale/tabelle-di-riferimento","tab")
    #Downloads single contents
    wGetAndRename("portale/documents/20182/26001/errori_anpr_20170301.xlsx/1e54c0fd-b77b-4980-9374-af6f05111578","Errori ANPR","error")
    wGetAndRename("portale/documents/20182/26001/Allegato+9+-+Esiti+AE.xlsx/05d05160-20e5-4afc-9ba9-07fde16c8044","Errori Agenzia Entrate","error")

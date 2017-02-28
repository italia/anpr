from lxml import html
import requests
import re
anpr_domain='https://www.anpr.interno.it/'
table_path='portale/tabelle-di-riferimento'
page = requests.get(anpr_domain+table_path)
tree = html.fromstring(page.content)


#xlxs = tree.xpath("//a[ends-with(@href,'.xlsx')]/@href")
regex = re.compile(r'.*\.xlsx$')
xlxs =  filter(regex.search, tree.xpath("//a[contains(@href,'.xlsx')]/@href"))
#XPATH expression to get all the exel files
allxlxs= tree.xpath("//a[contains(@href,'.xlsx')]")
print allxlxs
for xls in allxlxs:
    if xls.text is not None:
        print xls.get("href")  + xls.text

for xls in allxlxs:

    r = requests.get(anpr_domain+xls.get("href"), stream=True)
    print anpr_domain+xls.get("href")
    if r.status_code == 200:
        file_content = r.raw.read()
        print "Downloading: [" + xls.get("href") +"]"
        file_name= re.sub(r'([^.a-zA-Z0-9])','_',xls.text) +".xlsx".lower()
        path= "../xlsx/"+file_name
        with open(path, 'w') as f:
            f.write(file_content)

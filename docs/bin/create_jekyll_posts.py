import sys
import os
from openpyxl import load_workbook
from os import listdir
def convertXlsxToHtml(infn,outfn):
	wb = load_workbook(infn)
	f = open(outfn, "w")

	# grab the active worksheet
	ws = wb.active
	rows = []
	for i,row in enumerate(ws):

		cells = []
		for c in row:
			if c.value is None:
				cells.append("")
				continue
			description = c.value
			if type(description) == str:
			 		value = unicode(description,"utf-8")
			else:
				value = unicode(description)
			value = value.encode("utf-8")
			cells.append(value)
		rows.append(cells)



	print >>f,"<table class=\"Table Table--withBorder Table--compact u-text-r-xxs\">"
	headers = rows[0]
	print >>f,"<thead><tr>"
	#print >>f, "<th><a name=\""+headers[0]+"\">"+headers[0]+"</a></th>"
	for header in headers:
		print >>f, "<th>"+header+"</th>"
	print >>f,"</tr></thead><tbody>"
	for row in rows[1:]:
		print >>f,"<tr>"
		print >>f, "<th scope=\"row\"><a name=\""+row[0]+"\">"+row[0]+"</a></th>"
		for cell in row[1:]:
			print >>f, "<td>"+cell+"</td>"
		print >>f,"</tr>"

	print >>f,"</tbody></table>"
	f.close()

def getXlsxFiles(path_to_dir, suffix=".xlsx" ):
    filenames = listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith( suffix ) ]

if __name__ == "__main__":
	if len(sys.argv)<2 :
		print "Usage " + __file__ + " [Directory for xlsx files] [Directory for xlsx output]"
		quit()
	xlxs_folder =sys.argv[1]
	xlsx= getXlsxFiles(xlxs_folder)
	print xlsx
	for xls in xlsx:
		file_name = (xls[0:-5]).lower()
		print file_name
		section=file_name[:(file_name.index("_"))]
		title =  (file_name[(file_name.index("_")+1)::]).replace("_"," ").title()
		print "Title: "  + title
		convertXlsxToHtml(xlxs_folder+xls, sys.argv[2]+file_name+".html" )
		print "Creating Jekyll Posts for " + title +", section: "+ section
		os.system("ruby bin/jekyll-page \""+title+"\" "+section+" "+file_name+".html "+file_name+".html")

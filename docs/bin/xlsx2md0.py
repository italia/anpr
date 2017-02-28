import sys
from openpyxl import load_workbook

infn = sys.argv[1]
outfn = sys.argv[2]

wb = load_workbook(infn)
f = open(outfn, "w")

# grab the active worksheet
ws = wb.active
columns = []
for i,row in enumerate(ws):

	for c in row:
		if c.value is None:
			continue
		description = row[1].value
		if type(description) == str:
			value = unicode(description,"utf-8")
		else:
			value = unicode(description)

		value = value.encode("utf-8")
		print row[0].value + " " +row[1].value
		columns.append([row[0].value,value])

	#print >>f, "|"+"|".join(columns)+"|"
	#if i == 0:
print "<dl>"
for column in columns:
	print >>f, "<dd><a name=\""+column[0]+"\">"+column[0]+"</a>"
	print >>f, "<p>"+column[1]+"</p></dd>"

print "</dl>"

f.close()

import sys
from openpyxl import load_workbook

infn = sys.argv[1]
outfn = sys.argv[2]

wb = load_workbook(infn)
f = open(outfn, "w")

# grab the active worksheet
ws = wb.active

for i,row in enumerate(ws):
	columns = []
	for c in row:
		if c.value is None:
			continue

		if type(c.value) == str:
			value = unicode(c.value, "utf-8")
		else:
			value = unicode(c.value)

		value = value.encode("utf-8")
		columns.append(value)

	print >>f, "|"+"|".join(columns)+"|"
	if i == 0:
		print >>f, "|"+"|".join(["---"]*len(columns))+"|"

f.close()



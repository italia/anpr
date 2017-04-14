import sys
import os
import codecs
from openpyxl import load_workbook
from os import listdir

def convertXlsxToRst(infn,f, startFromRow=0,ncol =2):
    wb = load_workbook(infn)

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

            cells.append(value)
        rows.append(cells)



    headers = rows[startFromRow]
    print "headers", headers
    firstHeader = 0
    for i,r in enumerate(headers):
        if(len(r)>0):
            break
        firstHeader = firstHeader+1

    print "firsHeader",firstHeader
    size  = [10]* ncol
    maxCol = 400


    maxHeader = max([(len(u''+x),x) for x in headers])
    print "maxHeader", maxHeader
    for row in rows:
        for i in range((ncol-1),len(headers)):
            print "row", row
            lenRow_i = len(u''+row[i])
            print "i row len ",i, row[i], lenRow_i
            size[i]=max(size[i], lenRow_i)
            maxCol=max(maxCol, (lenRow_i+maxHeader[0]+20))



    print "maxCol:", maxCol
    size[ncol-1] = maxCol
    row_separator=('+'+'{:}+'*ncol).format(*[x*"-" for x in size]);

    fmt_row = u'|'+ '|'.join(["{:"+str(x)+"}" for x in size])+"|"

    print >>f, row_separator
    v= headers[:ncol]

    print >>f, fmt_row.format(*v)
    print >>f, ('+'+'{:}+'*ncol).format(*[x*"=" for x in size]);

    firstDataRow  = startFromRow+1
    for row in rows[firstDataRow:]:
        if not row[firstDataRow]:
            continue

        for i,v in enumerate(row):
                row[i] = v.replace("\n", " ")


        print "fmt_row", fmt_row, row,firstHeader, ncol,  row[firstHeader:(firstHeader+ncol)]
        print >>f,fmt_row.format(*row[firstHeader:(firstHeader+ncol)])

        for i, other_row in enumerate(row[firstHeader+ncol::]):
            if i ==0 :
                print >>f, fmt_row.format(*(['']*ncol))

            if len(other_row)>0:
                key = ""+headers[firstHeader+ncol+i]+ ": " if headers[firstHeader+ncol+i]   else  ""
                v = [""]*(ncol-1) +["  - "+key+  other_row]
                print >>f, fmt_row.format(*v)

        print >>f, row_separator

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

        f = codecs.open(sys.argv[2]+file_name+".rst", "w", "utf-8")
        convertXlsxToRst(xlxs_folder+xls, f)
        f.close()

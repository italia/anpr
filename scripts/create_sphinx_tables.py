import sys
import os
import codecs
from openpyxl import load_workbook
from os import listdir

def convertXlsxToRst(infn,f):
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
            # value = value.encode("utf-8")
            cells.append(value)
        rows.append(cells)


    #headers = rows[0]
    #ncol = len(rows[0])
    ncol =2
    # Compute filed with maximum width, to format the table correctly

    '''
+--------+--------------------+
| Header | Header with 2 cols |
+========+========+===========+
'''
    #fmt = "%-50s %-200s"
    #print fmt

    headers = rows[0]
    firstHeader = 0
    for i,r in enumerate(headers):
        if(len(r)>0):
            break
        firstHeader = firstHeader+1

    idSize= 10
    descSize = 600
    width = 0
    for row in rows:
        idSize = max(idSize, len(row[firstHeader]))

    print idSize
    row_separator = '+{}+{}+'.format("-"*idSize, "-"*descSize)
    fmt_row = u'|{:'+str(idSize)+'}|{:'+str(descSize)+'}|';

    #first header

    print fmt_row
    print >>f, row_separator
    print >>f, fmt_row.format(headers[firstHeader],headers[firstHeader+1])
    print >>f, '+{}+{}+'.format("="*idSize, "="*descSize)


    for row in rows[1:]:
        if not row[0]:
            continue

        for i,v in enumerate(row):
                row[i] = v.replace("\n", " ")

        print >>f,fmt_row.format(row[firstHeader],row[firstHeader+1])

        for i, other_row in enumerate(row[firstHeader+2::]):
            if other_row:
                key = ""+headers[firstHeader+2+i]+ ": " if headers[firstHeader+2+i]   else  ""
                print >>f, fmt_row.format("",  "  - "+key+  other_row)


        print >>f, row_separator

    #print >>f ,row_separator

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

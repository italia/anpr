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


    headers = rows[0]
    ncol = len(rows[0])
    ncol =2
    # Compute filed with maximum width, to format the table correctly
    width = 0
    for row in rows:
        width = max(width, max([len(c) for c in row])+10)

    fmt = " ".join(["%-" + str(width) + "s"] * ncol)
    '''
+--------+--------------------+
| Header | Header with 2 cols |
+========+========+===========+
''''
    #fmt = "%-50s %-200s"
    print fmt
    idSize= 20
    descSize = 200
    row_separator = '+{}+{}+'.format("-"*idSize, "-"*descSize)
    print >>f row_separator
    print >>f '|{:^'+str(idSize)'}|{^'+str(descSize)+'}|'.format("id","descrizione")
    print >>f '+{}+{}+'.format("="*idSize, "="*descSize)

    print >>f, fmt % (("="*width,)*ncol)
    print >>f, fmt % tuple(("ID","Descrizione"))
    print >>f, fmt % (("="*width,)*ncol)
    for row in rows[1:]:
        for i,v in enumerate(row):
                row[i] = v.replace("\n", " ")
        #is_empy
        row_adjusted = (row[0], row[1])
        print >>f '|{:^'+str(idSize)'}|{^'+str(descSize)+'}|'.format(row[0],row[1])

        for other_row in row[1::]:
            print >>f '|{:^'+str(idSize)'}|{^'+str(descSize)+'}|'.format("",other_row)


        #print >>f, fmt % tuple(row_adjusted)
        print >>f row_separator

    print >>f '+{}+{}+'.format("-"*idSize, "-"*descSize)

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

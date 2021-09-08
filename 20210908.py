# 一键隐藏电话号码和学号
import re

import openpyxl


path = 'data.xlsx'
wb = openpyxl.load_workbook(path)
sh = wb['Sheet1']

for row in list(sh.rows):
    # print(row.value)
    name = row[9].value
    for i in row[10:12]:
        if i.value!=None:
            name+=(','+i.value)
        pass
    print(name if name!= None else '')
    # print()

wb.save(path)
wb.close()
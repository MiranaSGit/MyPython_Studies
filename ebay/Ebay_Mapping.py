from openpyxl import load_workbook
import pandas as pd
import xlrd
import xlsxwriter
import os
import csv


# abspath = os.path.abspath(__file__)
# dname = os.path.dirname(abspath)      # that script in.
# os.chdir(dname)
# print(dname)

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)      # that script in.
os.chdir(dname)

filename = dname + "\Mapping.xlsx"

f = load_workbook(filename)
sheet = f['Sheet1']
listEbay = []
listShopify = []
for cell in sheet['A']:  # Printing Column A
    if cell.value != None:
        listShopify.append(cell.value)

for cell in sheet['B']:  # Printing Column A
    if cell.value != None:
        listEbay.append(cell.value)

# print(len(listEbay))
for i in listShopify:
    if i in listEbay:
        listEbay.remove(i)
# print(len(listEbay))


with open('Mapping_OUT.csv', mode='w', newline="") as new_file:
    writer = csv.writer(new_file, delimiter=',')
    writer.writerow(["SKU_Shopify", "ALT_SKU"])
    for i in listEbay:
        for j in listShopify:
            if str(i).endswith(str(j)):
                writer.writerow([j, i])

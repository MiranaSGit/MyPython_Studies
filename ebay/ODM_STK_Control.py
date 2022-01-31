import os
import csv

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
file_ODM = dname + "\mpStockFile.csv"

dictODM = {}
dictMAM = {}

tmpFile = "ODM_LWStock.csv"
with open(file_ODM, mode='r', newline="", encoding='utf-8') as inputfile:
    reader = csv.reader(inputfile, delimiter=',')
    header = next(reader)
    # writer.writerow(['SKU', 'Stock Level', 'Location'])
    for row in reader:
        if row[0].startswith("10-") or row[0].startswith("18-"):
            dictODM[row[0].strip()] = row[1].strip()

file_MAM = dname + "\ODM_MAM.csv"

with open(file_MAM, mode='r', newline="", encoding='utf-8') as inputfile:
    reader = csv.reader(inputfile, delimiter=',')
    header = next(reader)
    for row in reader:
        # if row[0] != "" or row[1] != "":
        if row[0] not in (None, ""):
            dictMAM[row[0].strip()] = row[1].strip()

# items which don't have a value is removed from the dict.
for i in dictMAM.copy().keys():
    if dictMAM[i] == "":
        dictMAM.pop(i)
for i in dictODM.keys():
    if i in dictMAM.keys():
        if int(dictODM[i]) < int(dictMAM[i]):
            dictODM[i] = dictMAM[i]

with open(tmpFile, mode='w', newline="", encoding='utf-8') as outfile:
    writer = csv.writer(outfile, delimiter=',')
    writer.writerow(['SKU', 'Stock Level', 'Location'])
    for i, j in dictODM.items():
        writer.writerow([i, j, 'MAIN_STOCK'])
    writer.writerow(['18-213051X2', dictODM['18-213051'], 'MAIN_STOCK'])
    if dictODM['18-041570'] >= dictODM['18-042570']:
        writer.writerow(['18-041570P', dictODM['18-042570'], 'MAIN_STOCK'])
    if dictODM['18-041570'] < dictODM['18-042570']:
        writer.writerow(['18-041570P', dictODM['18-041570'], 'MAIN_STOCK'])
    if dictODM['18-342101'] >= dictODM['18-341101']:
        writer.writerow(['18-342101P', dictODM['18-341101'], 'MAIN_STOCK'])
    if dictODM['18-342101'] < dictODM['18-341101']:
        writer.writerow(['18-342101P', dictODM['18-342101'], 'MAIN_STOCK'])
    if dictODM['18-342161'] >= dictODM['18-341161']:
        writer.writerow(['18-342161-P', dictODM['18-341161'], 'MAIN_STOCK'])
    if dictODM['18-342161'] < dictODM['18-341161']:
        writer.writerow(['18-342161-P', dictODM['18-342161'], 'MAIN_STOCK'])
    if dictODM['18-152340'] >= dictODM['18-151340']:
        writer.writerow(
            ['18-152340-151340', dictODM['18-151340'], 'MAIN_STOCK'])
    if dictODM['18-152340'] < dictODM['18-151340']:
        writer.writerow(
            ['18-152340-151340', dictODM['18-152340'], 'MAIN_STOCK'])
    if dictODM['18-011721'] >= dictODM['18-012721']:
        writer.writerow(
            ['18-011721+18-012721', dictODM['18-012721'], 'MAIN_STOCK'])
    if dictODM['18-011721'] < dictODM['18-012721']:
        writer.writerow(
            ['18-011721+18-012721', dictODM['18-011721'], 'MAIN_STOCK'])
    if dictODM['18-011850'] >= dictODM['18-012850']:
        writer.writerow(
            ['PAIR11850-12850', dictODM['18-012850'], 'MAIN_STOCK'])
    if dictODM['18-011850'] < dictODM['18-012850']:
        writer.writerow(
            ['PAIR11850-12850', dictODM['18-011850'], 'MAIN_STOCK'])

os.remove('mpStockFile.csv')
os.remove('ODM_MAM.csv')

with open('ODM_MAM.csv', mode='w', newline="", encoding='utf-8') as outfile:
    writer = csv.writer(outfile, delimiter=',')
    writer.writerow(['SKU', 'Stock Level'])

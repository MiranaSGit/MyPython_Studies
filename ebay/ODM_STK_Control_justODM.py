import os
import csv

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
file_ODM = dname + "\mpStockFile.csv"

listPairs = ['18-041570', '18-042570', '18-342101', '18-341101', '18-342161',
             '18-341161', '18-213051', '18-152340', '18-151340', '18-011721',
             '18-012721', '18-011850', '18-012850']
dictODM = {}

tmpFile = "ODM_LWStock.csv"
with open(file_ODM, mode='r', newline="", encoding='utf-8') as inputfile, \
        open(tmpFile, mode='w', newline="", encoding='utf-8') as outfile:
    reader = csv.reader(inputfile, delimiter=',')
    writer = csv.writer(outfile, delimiter=',')
    header = next(reader)
    writer.writerow(['SKU', 'Stock Level', 'Location'])
    for row in reader:
        if row[0] in listPairs:
            dictODM[row[0]] = row[1]
        if row[0].startswith("10-") or row[0].startswith("18-"):
            writer.writerow([row[0], row[1], 'MAIN_STOCK'])

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

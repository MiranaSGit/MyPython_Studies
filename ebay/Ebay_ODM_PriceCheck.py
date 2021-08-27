import os
import csv

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

listEBAY = []
listODM = []

for i in os.listdir("."):
    if i.startswith("eBay-active-listing"):
        with open(i, 'r', newline='', encoding="utf-8") as file:
            csv_rows = csv.reader(file)  # reader() function takes each
            # row (lines) into a list
            header = next(csv_rows)
            if header != None:   # Passing header row
                for row in csv_rows:
                    if row[3].startswith("10-") or row[3].startswith("18-"):
                        if row[3] not in listEBAY:
                            listEBAY.append(row[3])
                    if row[3].find("-18-") != -1 or row[3].find("-10-") != -1:
                        if row[3] not in listEBAY:
                            listEBAY.append(row[3])

# print(listEBAY)
# file_ODM = dname + "\mpStockFile.csv"

# with open(file_ODM, 'r', newline='', encoding='utf-8') as file:
#     csv_rows = csv.reader(file)  # reader() function takes each
#     # row (lines) into a list
#     header = next(csv_rows)
#     if header != None:   # Passing header row
#         for row in csv_rows:
#             if row[1] != str(0):
#                 listODM.append(row[0])


with open('TP_ODM_Items.csv', mode='w', newline="") as new_file:
    writer = csv.writer(new_file, delimiter=',')
    for i in listEBAY:
        writer.writerow([i])

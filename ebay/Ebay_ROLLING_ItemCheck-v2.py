import os
import csv
import pandas as pd
from openpyxl import load_workbook

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

listEBAY = []
listROLLING = []
listROLLING_DetayOlmayan = []

for i in os.listdir("."):
    if i.startswith("eBay-active-listing"):
        with open(i, 'r', newline='', encoding="utf-8") as file:
            csv_rows = csv.reader(file)  # reader() function takes each
            # row (lines) into a list
            header = next(csv_rows)
            if header != None:   # Passing header row
                for row in csv_rows:
                    if row[3].startswith("ALT") or row[3].startswith("STM") \
                            or row[3].startswith("VSBC") or row[3].startswith("VSEP"):
                        listEBAY.append(row[3])


file_ROLLING = dname + "\ROLLING STOCK LIST.xlsx"
file_ROLLING_DetayOlmayan = dname + "\ROLLING_DetayOlmayanlar.xlsx"

f = load_workbook(file_ROLLING_DetayOlmayan)
sheet = f.active
for cell in sheet['A']:  # Printing Column A
    if cell.value != None and cell.value != "SKU":
        listROLLING_DetayOlmayan.append(cell.value)
f.close()


book1 = pd.ExcelFile(file_ROLLING)
df = pd.read_excel(book1, sheet_name='Rotating')
for i in df.index:
    if not pd.isna(df['Comment'][i]) and df['Comment'][i] != "Out of stock":
        listROLLING.append(df['ROLLCO'][i])

df = pd.read_excel(book1, sheet_name='Brake Caliper')
for i in df.index:
    if not pd.isna(df['Comment'][i]) and df['Comment'][i] != "Out of stock":
        listROLLING.append(df['ROLLCO'][i])

with open('TPde_Olmayan_ROLLING_Items.csv', mode='w', newline="") as new_file:
    writer = csv.writer(new_file, delimiter=',')
    for i in listROLLING:
        if i not in listEBAY and i not in listROLLING_DetayOlmayan:
            writer.writerow([i])

import os
import csv
import pandas as pd

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

listEBAY = []
listROLLING = []

for i in os.listdir("."):
    if i.startswith("FileExchange"):
        filename = i
        with open(filename, 'r', newline='') as file:
            csv_rows = csv.reader(file)  # reader() function takes each
            # row (lines) into a list
            header = next(csv_rows)
            if header != None:   # Passing header row
                for row in csv_rows:
                    if row[10].startswith("ALT") or row[10].startswith("STM") \
                            or row[10].startswith("VSBC") or row[10].startswith("VSEP"):
                        listEBAY.append(row[10])


file_ROLLING = dname + "\ROLLING STOCK LIST.xlsx"
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
        if i not in listEBAY:
            writer.writerow([i])

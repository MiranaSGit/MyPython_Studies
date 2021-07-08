import csv
import os
import pandas as pd

# Setting working directory to the directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)      # that script in.
os.chdir(dname)


for i in os.listdir("."):
    if i.startswith("ROLLING"):
        file = i
        break


rolling_inventory = {}

book1 = pd.ExcelFile(file)

df = pd.read_excel(book1, sheet_name='Rotating')

for i in df.index:
    if df['Comment'][i] == 'In Stock':
        rolling_inventory[df['ROLLCO'][i]] = 4
    elif df['Comment'][i] == 'Low Stock':
        rolling_inventory[df['ROLLCO'][i]] = 1
    elif df['Comment'][i] == 'Out of stock':
        rolling_inventory[df['ROLLCO'][i]] = 0
    else:
        pass

book2 = pd.ExcelFile(file)

df = pd.read_excel(book1, sheet_name='Brake Caliper')

for i in df.index:
    if df['Comment'][i] == 'In Stock':
        rolling_inventory[df['ROLLCO'][i]] = 4
    elif df['Comment'][i] == 'Low Stock':
        rolling_inventory[df['ROLLCO'][i]] = 1
    elif df['Comment'][i] == 'Out of stock':
        rolling_inventory[df['ROLLCO'][i]] = 0
    else:
        pass


if rolling_inventory['VSBC164L'] < rolling_inventory['VSBC164R']:
    rolling_inventory['VSBC164L+VSBC164R'] = rolling_inventory['VSBC164L']
else:
    rolling_inventory['VSBC164L+VSBC164R'] = rolling_inventory['VSBC164R']

with open('ROLLING_LW.csv', mode='w', newline="") as new_file:
    writer = csv.writer(new_file, delimiter=',')
    writer.writerow(["SKU", "Stock Level", "Location"])
    for i, j in rolling_inventory.items():
        writer.writerow([i, j, "MAIN_STOCK"])

# Have to delete book files to deleted the red file as it is still in memory.
del book1
del book2

filename_toBeDeleted = str(dname) + "\\ROLLING STOCK LIST.xlsx"
if os.path.isfile("ROLLING STOCK LIST.xlsx"):
    os.remove(filename_toBeDeleted)

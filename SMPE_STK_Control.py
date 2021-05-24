import csv
import os

# Setting working directory to the directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)      # that script in.
os.chdir(dname)

filename = str(dname) + "\\new_file.csv"
if os.path.isfile("new_file.csv"):
    os.remove(filename)

for i in os.listdir("."):
    if i.startswith("231"):
        file = i
        break

smpe_inventory = {}

with open(file, "r") as csv_file:
    reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for line in reader:
        if line_count == 0:
            line_count += 1
        else:
            part_no = line[0]
            stock_level = line[6]
            if stock_level == "Good":
                smpe_inventory[part_no] = 10
            elif stock_level == "Less than 10":
                smpe_inventory[part_no] = 5
            elif stock_level == "Less than 5":
                smpe_inventory[part_no] = 2
            else:
                smpe_inventory[part_no] = 1

myLW_Stock = {}

with open("TP_SMPE_SKU.csv", "r") as csv_file2:
    reader = csv.reader(csv_file2)
    for i in reader:
        if i[0] in smpe_inventory.keys():
            myLW_Stock[i[0]] = smpe_inventory[i[0]]
        else:
            myLW_Stock[i[0]] = 0


with open('new_file.csv', mode='w', newline="") as new_file:
    writer = csv.writer(new_file, delimiter=',')
    writer.writerow(["Stock Level", "SKU", "Location"])
    for i, j in myLW_Stock.items():
        writer.writerow([i, j, "MAIN_STOCK"])


filename = str(dname) + "\\" + str(file)
os.remove(filename)

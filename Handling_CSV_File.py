import csv
import os

# Setting working directory to the directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)      # that script in.
os.chdir(dname)

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

with open('my_ofd.csv', mode='w', newline="") as file:
    writer = csv.writer(file, delimiter=',')
    for i, j in smpe_inventory.items():
        writer.writerow([i, j])

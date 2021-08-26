from csv import DictReader
import csv  # loads csv module
import os

# Setting working directory to the directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)      # that script in.
os.chdir(dname)

filename = dname + "\\WorkingWithFiles\\fruits.csv"
print(filename)

with open(filename, 'r', newline='', encoding='utf-8') as file:
    csv_rows = csv.reader(file)  # reader() function takes each
    # row (lines) into a list
    for row in csv_rows:
        print(row)


# We can also display each row in the list as a single string. If we determine a
# character that is not included in the CSV file and allocate this character as the
# value of delimiter, we can print all lines of the CSV file as lists as a single
# string element. Consider this one :

with open(filename, 'r', newline='', encoding='utf-8') as file:
    # we specified a char ":" that is not used
    csv_rows = csv.reader(file, delimiter=':')
    # in the csv file as a value of delimiter
    for row in csv_rows:
        print(row)


# With csv module’s DictReader class object we can iterate over the lines of a csv file as a dictionary i.e.
# for each row a dictionary is returned, which contains the pair of column names and cell values for that row.
# Let’s understand with an example,


# from csv import DictReader
# open file in read mode
with open('students.csv', 'r') as read_obj:
    # pass the file object to DictReader() to get the DictReader object
    csv_dict_reader = DictReader(read_obj)
    # iterate over each line as a ordered dictionary
    for row in csv_dict_reader:
        # row variable is a dictionary that represents a row in csv
        print(row)


with open('Mapping_OUT.csv', mode='w', newline="") as new_file:
    writer = csv.writer(new_file, delimiter=',')
    writer.writerow(["SKU_Shopify", "ALT_SKU"])
    for i in listEbay:
        for j in listShopify:
            if str(i).endswith(str(j)):
                writer.writerow([j, i])

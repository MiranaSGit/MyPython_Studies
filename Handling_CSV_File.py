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

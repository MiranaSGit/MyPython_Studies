import os
import glob
import shutil
os.listdir()

for file in glob.glob("*.py"):
    print(file)

shutil.copy("Calculator.py", "../Calculator_new.py")

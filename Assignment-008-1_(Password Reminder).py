# Task : Let's say; you left a message in the past that prints a password you need. 
# To see the password you wrote, you need to enter your name and the program should recognize you.
# Write a program that 
# 
# 1- Takes the first name from the user and compares it to yours,
# 2- Then if the name the user entered is the same as yours, print out such as : "Hello, Joseph! 
# 3- The password is : W@12",
# If the name the user entered is not the same as yours, print out such as : "Hello, Amina! 
# See you later."
my_name = "Faruk"
name = input("Please enter your name: ").title()
if name == my_name:
    print("Hello, {}! The password is : W@12frk".format(nameFAru))
else:
    print("Hello, {}! See you later.".format(name))

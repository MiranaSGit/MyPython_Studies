# Task:
# 
# Find out if a given number is an "Armstrong Number".
# 
# An n-digit number that is the sum of the nth powers of its digits is 
# called an n-Armstrong number. Examples:
# 371 = 3^3 + 7^3 + 1^3
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
# 93084 = 9^5 + 3^5 + 0^5 + 8^5 + 4^5.
# 
# Write a Python program that
# takes a positive integer number from the user,
# checks the entered number if it is Armstrong,
# consider the negative, float and any entries other than numeric values 
# then display a warning message to the user.

remaining = 0
body = 0
my_list = []
temp = 0
count= 0
sum = 0
while True:
    num = int(input("Please enter a positive number: "))
    if num <= 0:
        print("Number must be positive! Try again. ")
    else:
        temp = num
        break
while True:
    body = temp // 10
    remaining = temp % 10
    my_list.append(remaining)
    count += 1
    if body == 0:
        newList = my_list[::-1]
        break
    else: 
        temp = body
        continue
# print(newList, count)
for i in newList:
    sum += pow(i, count)
if sum == num:
    print("{} is an Armstrong Number.".format(num))
else:
    print("{} is not an Armstrong Number.".format(num))

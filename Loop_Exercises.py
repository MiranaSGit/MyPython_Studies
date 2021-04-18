print(*range(11), sep="\n")

# Exercise 2: Print the following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
i = j = 1
while i < 6:
    j = 1
    print("")
    while j <= i:
        print(j, end = " ")
        j += 1
    i += 1
print()

#Alternative Solution
# print("Second Number Pattern ")
# lastNumber = 6
# for row in range(1, lastNumber):
#     for column in range(1, row + 1):
#         print(column, end=' ')
#     print("")




# Exercise 3: Accept number from user and calculate the sum of all number from 1 to a given number
# For example, if user entered 10 the output should be 55.
sum1 = 0
n = int(input("Please enter number "))
for i in range(1, n + 1, 1):
    sum1 += i
print("\n")
print("Sum is: ", sum1)
print()



# Exercise 4: Print multiplication table of a given number
n = 2
for i in range(1, 11, 1):
    product = n*i
    print(product)



# Exercise 5: Given a list, iterate it, and display numbers divisible by five, and if you find 
# a number greater than 150, stop the loop iteration.
list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
# Expected output:
# 15
# 55
# 75
# 150
for i in list1:
    if i <= 150 and i % 5 == 0:
        print(i)
    else:
        continue

# Alternative Solution
# for item in list1:
#     if (item > 150):
#         break
#     if(item % 5 == 0):
#         print(item)


# Exercise 6: Given a number count the total number of digits in a number
# For example, the number is 75869, so the output should be 5.
num = 75869
count = 0
while num != 0:
    num //= 10
    count += 1
print("Total digits are: ", count)


# Exercise 7: Print the following pattern using for loop
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print("")

# Alternative Solution
# n = 5
# k = 5
# for i in range(0, n+1):
#     for j in range(k-i, 0, -1):
#         print(j, end=' ')
#     print()


# Exercise 8: Reverse the following list using for loop
list1 = [10, 20, 30, 40, 50]
lenght = len(list1)
list2 = []
for i in range(lenght - 1, -1, -1):
    list2.append(list1[i])
print(list2)


# Exercise 9: Display numbers from -10 to -1 using for loop
for i in range(-10, 0, 1):
    print(i)


# Exercise 10: Display a message “Done” after successful execution of for loop
for i in range(0, 6):
    print(i)
    if i == (len(range(0, 6)) - 1):
       print("Done!")

# Alternative Solution
# for i in range(5):
#     print(i)
# else:
#     print("Done!")




   
# Exercise 11: Write a program to display all prime numbers within a range
# start = 25
# end = 50
# Expected output:
#
# Prime numbers between 25 and 50 are:
# 29
# 31
# 37
# 41
# 43
# 47
for i in range(25, 51):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)




# Exercise 12: Display Fibonacci series up to 10 terms
# Expected output:
#
# Fibonacci sequence:
# 0  1  1  2  3  5  8  13  21  34
list = [0, 1]
# new_list = []
count = 1
print("Fibonacci sequence:")
while count < 9:
    lenght = len(list)
    sum = 0
    for i in range(lenght - 2, lenght):
        sum += list[i]
    count += 1
    list.append(sum)
    print(list)
#print(list)

# Alternative Solution
# terms = 10
# # first two terms
# num1, num2 = 0, 1
# count = 0
# 
# print("Fibonacci sequence:")
# while count < terms:
#     print(num1, end="  ")
#     temp = num1 + num2
#     # update values
#     num1 = num2
#     num2 = temp
#     count += 1






# Exercise 13: Write a loop to find the factorial of any number
# The factorial(symbol: !) means to multiply all whole numbers from the chosen number down to 1.
#
# For example: calculate the factorial of 5
#
# 5! = 5 × 4 × 3 × 2 × 1 = 120
# Expected output:
#
# 120
num = int(input("Enter the number to be calculated its factorial: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of {} is: {}".format(num, factorial))




# Exercise 14: Reverse a given integer number
num = int(input("Please enter a number: "))
temp = str(num)
print(temp[::-1])

# Alternative Solution
# num = 76542
# reverse_number = 0
# print("Given Number ", num)
# while num > 0:
#     reminder = num % 10
#     reverse_number = (reverse_number * 10) + reminder
#     num = num // 10
# print("Revered Number ", reverse_number)





# Exercise 15: Use a loop to display elements from a given list that are present at
# even index positions
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Expected output:
# 20 40 60 80 100
lenght = len(my_list)
new_list = []
for i in range(1, lenght, 2):
    new_list.append(my_list[i])
print(new_list)

# Alternative Solution
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for i in my_list[1::2]:
#     print(i, end=" ")





# Exercise 16: Display the cube of the number up to a given integer
num = int(input("Please a number for the cube calculation: "))
for i in range(1, num + 1):
    print("Current number is: {} and the cube is {}".format(i, i * i * i))




# Exercise 17: Find the sum of the series 2 + 22 + 222 + 2222 + .. n terms
# Given: number_of_terms = 5
# So series will become 2 + 22 + 222 + 2222 + 22222
#
# Expected output:
# 24690
sum = 0
for i in range(1, 6):
    str = i*"2"
    num = int(str)
    sum += num
print(sum)

# Alternative Solution
# number_of_terms = 5
# start = 2
# sum = 0
# for i in range(0, number_of_terms):
#     print(start, end=" ")
#     sum += start
#     start = (start * 10) + 2
# print("\nSum of above series is:", sum)


# Exercise 18: Print the following pattern
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
for i in range(1, 10):
    if i <= 5:
        print(i * "*", end=" ")
        print("")
    else:
        print((10-i) * "*", end=" ")
        print("")

# Alternative Solution
# rows = 5
# for i in range(0, rows):
#     for j in range(0, i + 1):
#         print("*", end=' ')
#     print("\r")
# 
# for i in range(rows, 0, -1):
#     for j in range(0, i - 1):
#         print("*", end=' ')
#     print("\r")

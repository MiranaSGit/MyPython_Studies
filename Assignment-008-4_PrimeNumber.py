# Task : Write a program that takes a number from the user and prints the result to check
# if it is a prime number.
# 
# The examples of the desired output are as follows :
# 
# input →  19 ⇉ output : 19 is a prime number
# input →  10 ⇉ output : 10 is not a prime number
# Note that ⚠: This question is famous on the web, so to get more benefit 
# from this assignment, try to complete this task on your own. 
num = int(input("Please provide a number: "))
count = 0
for i in range(2, num):
    if num % i == 0:
        count += 1
        print("{} is not a prime number". format(num))
        break
    else:
        continue
if count == 0:
    print("{} is a prime number". format(num))

# Alternative Solution:
def isPrime(n):

    # Corner case
    if n <= 1:
        return False

    # check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False

    return True
isPrime(23)

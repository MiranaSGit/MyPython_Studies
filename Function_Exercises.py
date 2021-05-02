# Exercise 1: Create a function that can accept two arguments name and age 
# and print its value
def myFunction(name, age):
    print("Name is: ", age, "\n", "Age is:", age)
myFunction("omer", 20)

   



# Exercise 2: Write a function func1() such that it can accept a variable length of 
# argument and print all arguments value
func1(20, 40, 60)
func1(80, 100)
# Expected Output:
# 
# func1(20, 40, 60)
# 20
# 40
# 60
# 
# func1(80, 100)
# 80
# 100
def func1(*args):
    for i in args:
        print(i)
    




# Exercise 3: Write a function calculation() such that it can accept two variables
#  and calculate the addition and subtraction of them. And also it must return both addition and subtraction in a single return call
# Given:
# def calculation(a, b):
#     # Your Code
# res = calculation(40, 10)
# print(res)
# Expected Output
# 50, 30
def calculation(a, b):
    return a + b, a - b
res = calculation(40, 10)
print(res)

# Alternative Solution
def calculation(a, b):
    return a+b, a-b
add, sub = calculation(40, 10)
print(add)
print(sub)


# Exercise 4: Create a function showEmployee() in such a way that it should accept employee 
# name, and its salary and display both. If the salary is missing in the function call assign
# default value 9000 to salary
# Given:
# 
# showEmployee("Ben", 9000)
# showEmployee("Ben")
# Expected output:
# 
# Employee Ben salary is: 9000
# Employee Ben salary is: 9000
def showEmployee(name, salary=9000):
    print("Employee ", name, " salary is: ", salary)
showEmployee("Ben", 9000)
showEmployee("Ben")




# Exercise 5: Create an inner function to calculate the addition in the following way
# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return itdef outerFunc(a, b):
def outerFunc(a, b):
    def innerFunc(a, b):
        return a + b
    add = innerFunc(a, b)
    return add + 5

outerFunc(10, 10)


# Exercise 7: Assign a different name to function and call it through the new name
# Below is the function displayStudent(name, age). Assign a new name showStudent(name, age)
#  to it and call through the new name
# def displayStudent(name, age):
#     print(name, age)
# 
# displayStudent("Emma", 26)
# You should be able to call the same function using
# 
# showStudent(name, age)
def displayStudent(name, age):
    print(name, age)

displayStudent("Emma", 26)

showStudent = displayStudent
showStudent("Emma", 26)





# Exercise 8: Generate a Python list of all the even numbers between 4 to 30
def myFunc(a, b):
    for i in range(a, b):
        list.append(i)
    print(list[::2])

myFunc(4, 30)



# Write a Python function that takes a list and returns a new list with unique 
# elements of the first list.
def fun(a):
    myList = []
    for i in a:
        if i not in myList:
            myList.append(i)
    return myList
print(fun([1, 2, 3, 3, 3, 3, 4, 5]))





# Write a Python function that takes a number as a parameter and check the number 
# is prime or not.
def prime_no(x):
    for i in range(2, x):
        if not x % i:
            return print(x, "is a not prime number.")
    return print(x, "is a prime number.")

prime_no(int(input("Input a number: ")))




# 4 math operation:
def func(a, b, op):
    if op == "+":
        return (a + b)
    elif op == "-":
        return (a - b)
    elif op == "*":
        return (a * b)
    elif op == "/":
        return (a / b)
    else:
        print("Enter a vlid operator!")


func(2, 3, "+")



# ARmstrong number 
# 371 = 3^3 + 7^3 + 1^3
while True:
    number = input("enter a positive number.")
    digits = len(number)
    summ = 0
    if not number.isdigit():
        print(number, "is invalid entry. enter numberic value!")
    elif int(number) >= 0:
        for i in range(digits):
            summ = summ + int(number[i]) ** digits
        if summ == int(number):
            print(number, "is an Armstrong Number.")
            break
        else:
            print(number, "is not an Armstrong Number.")
            break






# Write a Python function to multiply all the numbers in a list
def myFunc(t):
    sum = 1
    for i in t:
        sum *= i
    return sum

sample_list = (8, 2, 3, -1, 7)
myFunc(sample_list)




# Write a Python program to reverse a string.
def myFunc(a):
    return a[::-1]

text = "1234abcd"
myFunc(text)




# Write a Python function to calculate the factorial of a number 
# (a non-negative integer). The function accepts the number as an argument.
def myFunc(f):
    fac = 1
    for i in range(1, f + 1):
        fac *= i
    return fac


num = int(input("Please give a positive number: "))
myFunc(num)




# Write a Python function to check whether a number is in a given range.
def myFunc(f):
    if f in range(3, 9):
        return True
    else:
        return False

num = int(input("Please give a positive number: "))
myFunc(num)




# Write a Python function that accepts a string and calculate the number of 
# upper case letters and lower case letters.
def myFunc(f):
    up = 0
    low = 0
    for i in f:
        if i.isupper():
            up += 1
        elif i == " ":
            continue
        else:
            low +=1
    print("Number of uppercase is {}".format(up))
    print("Number of uppercase is {}".format(low))
text = 'The quick Brow Fox'
myFunc(text)

# Alternative Solution
def string_test(s):
    d = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"] += 1
        elif c.islower():
           d["LOWER_CASE"] += 1
        else:
           pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["UPPER_CASE"])
    print("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('The quick Brown Fox')





# Write a Python function to check whether a number is perfect or not.
def perfect(n):
    myList = []
    for i in range(1, n):
        if not n % i:
            myList.append(i)
        else:
            pass
    if sum(myList) == n:
        print(n, "is a perfect number.")
    else:
        print(n, "is not a perfect number.")

n = int(input("Input a number to check it is perfect or not: "))
perfect(n)

# Alternative Solution
def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n

print(perfect_number(6))





# Write a Python function that checks whether a passed string is palindrome or not.
# Note: A palindrome is a word, phrase, or sequence that reads the same backward 
# as forward, e.g., madam or nurses run.
def isPalindrome(string):
	left_pos = 0
	right_pos = len(string) - 1

	while right_pos >= left_pos:
		if not string[left_pos] == string[right_pos]:
			return False
		left_pos += 1
		right_pos -= 1
	return True

print(isPalindrome('aza'))


# Create a third-string made of the first char of s1 then the last char of s2, 
# Next, the second char of s1 and second last char of s2, and so on. Any leftover
# chars go at the end of the result.
def mixString(s1, s2):
  s2 = s2[::-1]
  lengthS1 = len(s1)
  lengthS2 = len(s2)
  length = lengthS1 if lengthS1 > lengthS2 else lengthS2
  resultString = ""
  for i in range(length):
    if(i < lengthS1):
      resultString = resultString + s1[i]
    if(i < lengthS2):
      resultString = resultString + s2[i]
  print(resultString)

s1 = "Abc"
s2 = "Xyzafg"
mixString(s1, s2)





# Checking vowels in an input
def myFunc(a):
    list = ["a", "e", "ı", "i", "o", "ö", "u", "ü"]
    result = []
    for i in a:
        if i in list:
            if i in result:
                pass
            else:
                result.append(i)
    return result
myFunc("benim olroho")

# Alternative Solution
def myFunc(a):
    list = ["a", "e", "ı", "i", "o", "ö", "u","ü"]
    if a.lower() in list:
        return True
    else:
        return False
sentence = "clarusway"
filtered_myFunc = filter(myFunc, sentence)
print(*filtered_myFunc)



# Defining a docstring in a function
def absolute(num):
    """
    This function returns the absolute value of
    the entered number
    """
    if num >= 0:
        return num
    else:
        return -num

print(absolute.__doc__)
absolute(-11)


# odds and even numbers from a given input
def slicer(*a):
    list1 = []
    list2 = []
    for i in a:
        if not i % 2:
            list1.append(i)
        else:
            list2.append(i)
    print(list1)
    print(list2)

slicer(1, 2, 3, 4, 5, 6, 7, 8, 9)

# Alternative Solution
def slicer(*a):
    print("evens: ", [i for i in a if i % 2 == 0])
    print("odds: ", [i for i in a if i % 2 != 0])
slicer(1, 2, 3, 4, 5, 6, 7, 8, 9)




# Kwargs example
def organizer(**a):
    names = []
    ages = []
    for i, j in a.items():
        names.append(i)
        ages.append(j)
    print(names)
    print(ages)
organizer(Beth = 26, Oscar = 42, Justin = 18, Frank = 33)

# Alternative Solution
def organizer(**a):
    print("names: ", [i for i in a.keys()])
    print("ages: ", [j for j in a.values()])

organizer(Beth=26, Oscar=42, Justin=18, Frank=33)


# İçerisine iki tane liste alan, listelerdeki rakamları tersten sayı şekline çevirip onları
#  toplayan ve toplamın rakamlarını tersten listeleyen fonksiyon yazıcaz. Listeler boş olamaz.
# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
list1 = [5, 6, 7, 8, 0, 2]
list2 = [3, 9, 1, 4, 4]

def rev(a):
    txt = [str(i) for i in a[::-1]]
    num = int("".join(txt))
    return num

def listing(a):
    txt = str(a)
    list = [i for i in txt[::-1]]
    return list

out = (rev(list1) + rev(list2))
listing(out)



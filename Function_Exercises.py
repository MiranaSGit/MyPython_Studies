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

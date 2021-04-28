# Code for the following alphabet A character

#      ***
#     *   *
#     *   *
#     *****
#     *   *
#     *   *
#     *   *

result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):    
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str)


# Code for returning an odd number of repetetive items in a given list
numbers_list = [2, 3, 4, 12, 7, 11, 2, 3, 7, 5, 12, 2, 5, 7, ]
newList = []
for i in numbers_list:
    if numbers_list.count(i) % 2:
        if i not in newList:
            newList.append(i)
print(newList)


# For the numbers 1-50, write a code that gives "Fizz" if it can be divided by 3, "Buzz" by 5
# and "FizzBuzz" both by 5 and 3.
list = []
for i in range(1,51):
    # print(i)
    if not i % 3 and not i % 5:
        list.append("FizzBuzz")
    elif not i % 3:
        list.append("Buzz")
    elif not i % 5:
        list.append("Fizz")
    else:
        list.append(i)
print(list)




# Code which floats the given item to left or right based on the given index num.
list = [0, 5, 16, 27, 32, 39, 42, 51]
# newList = []
index = int(input("Please provide an index num: "))
newList = list[-(index):] + list[:-(index)]
print(newList)


# Given a list, iterate it, and display numbers divisible by five, and if you find a 
# number greater than 150, stop the loop iteration.
list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for i in list1:
    if i <= 150 and not i % 5:
        print(i)

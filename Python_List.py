#Exercise 1
aLsit = [100, 200, 300, 400, 500]
# Expected outout [500, 400, 300, 200, 100]
print(aLsit[::-1])

# Exercise 2: Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
# Expected output: ['My', 'name', 'is', 'Kelly']

list3 = [i + j for i, j in zip(list1, list2)]
print(list3)


# Exercise 3: Given a Python list of numbers. Turn every item of a list into its square
aList = [1, 2, 3, 4, 5, 6, 7]
#Expected output: [1, 4, 9, 16, 25, 36, 49]
b = []
for i in aList: 
  b.append(i * i)
print(b)

#Alternative Solution
# aList =  [x * x for x in aList]
# print(aList)


# Exercise 4: Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
# Expected output: ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
list3 = []
for i in list1:
    for j in list2:
        list3.append(i+ " " + j)
print(list3)

#Alternative Solution
# resList = [x+y for x in list1 for y in list2]
# print(resList)


# Exercise 5: Given a two Python list. Iterate both lists simultaneously such that list1
# should display item in original order and list2 in reverse order
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
# Expected output:
# 10 400
# 20 300
# 30 200
# 40 100
for x, y in zip(list1, list2[::-1]):
    print(x, y)


#Exercise 6: Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
#Expected output: ["Mike", "Emma", "Kelly", "Brad"]
new_list = []
for i in list1:
    if i != "":
        new_list.append(i)
print(new_list)

# Alternative Solution
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# resList = list(filter(None, list1))
# print(resList)



# Exercise 7: Add item 7000 after 6000 in the following Python List
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
#Expected output: [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)



# Exercise 8: Given a nested list extend it by adding the sub list ["h", "i", "j"]
# in such a way that it will look like the following list
# Given List: 
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# Sub List to be added = ["h", "i", "j"]
# Expected output:['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
list_add = ["h", "i", "j"]
list1[2][1][2].extend(list_add)
print(list1)


# Exercise 9: Given a Python list, find value 20 in the list, and if it is present, 
# replace it with 200. Only update the first occurrence of a value
list1 = [5, 10, 15, 20, 25, 50, 20]
# Expected output: list1 = [5, 10, 15, 200, 25, 50, 20]
index = list1.index(20)
list1[index] = 200
print(list1)


# Exercise 10: Given a Python list, remove all occurrence of 20 from the list
list1 = [5, 20, 15, 20, 25, 50, 20]
# Expected output: [5, 15, 25, 50]
a = 0
for i in list1:
    if list1.count(i) > 1:
        while a < list1.count(i):
            list1.remove(i)
        i += 1
print(list1)

# Alternative Solution
# def removeValue(sampleList, val):
#    return [value for value in sampleList if value != val]
# resList = removeValue(list1, 20)
# print(resList)

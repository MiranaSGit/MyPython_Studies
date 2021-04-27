# Exercise 1: Reverse the following tuple
aTuple = (10, 20, 30, 40, 50)
print(aTuple[::-1])




# Exercise 2: Access value 20 from the following tuple
aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
print(aTuple[1][1])




# Exercise 3: Create a tuple with single item 50
myTuple = (50,)




# Exercise 4: Unpack the following tuple into 4 variables
aTuple = (10, 20, 30, 40)
a, b, c, d = aTuple
print(a, b, c, d)




# Exercise 5: Swap the following two tuples
tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1, tuple2 = tuple2, tuple1
print(tuple2)
print(tuple1)




# Exercise 6: Copy element 44 and 55 from the following tuple into a new tuple
tuple1 = (11, 22, 33, 44, 55, 66)
# Expected output:
# tuple2: (44, 55)
tuple2 = tuple1[3:5]
print(tuple2)





# Exercise 7: Modify the first item(22) of a list inside a following tuple to 222
tuple1 = (11, [22, 33], 44, 55)
# Expected output:
# tuple1: (11, [222, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)




# Exercise 8: Sort a tuple of tuples by 2nd item
tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
# Expected output:
# (('c', 11), ('a', 23), ('d', 29), ('b', 37))
sorted(tuple1, key=lambda x: x[1])
newTuple = sorted(tuple1, key=lambda x: x[1])
print(newTuple)




# Exercise 9: Counts the number of occurrences of item 50 from a tuple
tuple1 = (50, 10, 60, 70, 50)
# Expected output:
# 2
print(tuple1.count(50))




# Exercise 10: Check if all items in the following tuple are the same
tuple1 = (45, 45, 45, 45)
# Expected output:
# True
count = 0
tuple1 = (45, 45, 45, 45)
temp = ""
for i in tuple1:
    if tuple1.index(i) == 0:
        temp = i
        count += 1
    else:
        if i == temp:
            count += 1
            temp = i
        else:
            continue
print(count)
if count == len(tuple1):
    print("All items are the same!")
else:
    print("All items are not the same!")

# Alternative Solution
# def check(sampleTuple):
#     return all(i == sampleTuple[0] for i in sampleTuple)
# tuple1 = (45, 45, 45, 45)
# print(check(tuple1))

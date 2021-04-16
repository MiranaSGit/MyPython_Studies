# Exercise 2: Access value 20 from the following tuple
aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
# Expected output: 20
print(aTuple[1][1])

# Exercise 4: Unpack the following tuple into 4 variables
aTuple = (10, 20, 30, 40)
# Expected output:
# Your code
# print(a) # should print 10
# print(b) # should print 20
# print(c) # should print 30
# print(d) # should print 40
a, b, c, d = aTuple
print(a)
print(b)
print(c)
print(d)

#Exercise 5: Swap the following two tuples
tuple1 = (11, 22)
tuple2 = (99, 88)
#Expected output:
# tuple1 = (99, 88)
# tuple2 = (11, 22)
tuple1, tuple2 = tuple2, tuple1
print(tuple1)
print(tuple2)


# Exercise 6: Copy element 44 and 55 from the following tuple into a new tuple
tuple1 = (11, 22, 33, 44, 55, 66)
# Expected output:
# tuple2: (44, 55)
tuple2 = tuple1[3:5]
print(tuple2)

# Exercise 7: Modify the first item (22) of a list inside a following tuple to 222
tuple1 = (11, [22, 33], 44, 55)
# Expected output:
# tuple1: (11, [222, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)

# Exercise 8: Sort a tuple of tuples by 2nd item
tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
# Expected output:
# (('c', 11), ('a', 23), ('d', 29), ('b', 37))
sorted(tuple1, key=lambda x: x[1])
print(tuple1)

# Exercise 9: Counts the number of occurrences of item 50 from a tuple
tuple1 = (50, 10, 60, 70, 50)
# Expected output:2
print(tuple1.count(50))

# Exercise 10: Check if all items in the following tuple are the same
tuple1 = (45, 45, 45, 45)
# Expected output:True
for i in tuple1:
    for j in tuple1:
        if i == j:
            result = True
print(result)
#Alternative Solution
# def check(sampleTuple):
#     return all(i == sampleTuple[0] for i in sampleTuple)
# 
# tuple1 = (45, 45, 45, 45)
# print(check(tuple1))

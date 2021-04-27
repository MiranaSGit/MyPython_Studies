# Exercise 1: Add a list of elements to a given set
# Given:
sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]
# Expected output:
# Note: Set is unordered.
# {'Green', 'Yellow', 'Black', 'Orange', 'Red', 'Blue'}
sampleSet.update(sampleList)
print(sampleSet)




# Exercise 2: Return a new set of identical items from a given two set
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
# Expected output:
# 
# {40, 50, 30}
print(set1.intersection(set2))




# Exercise 3: Returns a new set with all items from both sets by removing duplicates
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
# Expected output:
# 
# {70, 40, 10, 50, 20, 60, 30}
set3 = set1.union(set2)
print(set3)



# Exercise 4: Given two Python sets, update the first set with items that exist only in the 
# first set and not in the second set.
set1 = {10, 20, 30}
set2 = {20, 40, 50}
# Expected output:
# set1 {10, 30}
set1.difference_update(set2)
print(set1)




# Exercise 5: Remove items 10, 20, 30 from the following set at once
set1 = {10, 20, 30, 40, 50}
# Expected output:
# {40, 50}
set1.difference_update({10, 20, 30})
print(set1)


# Exercise 6: Return a set of all elements in either A or B, but not both
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
# Expected output:
# {20, 70, 10, 60}
print(set1.symmetric_difference(set2))




# Exercise 7: Check if two sets have any elements in common. If yes, display the common elements.
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
# Expected output:
# Two sets have items in common
# {10}
if set1.isdisjoint(set2):
  print("Two sets have no items in common")
else:
  print("Two sets have items in common")
  print(set1.intersection(set2))




# Exercise 8: Update set1 by adding items from set2, except common items
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
# Expected output:
# {70, 10, 20, 60}
set1.symmetric_difference_update(set2)
print(set1)



# Exercise 9: Remove items from set1 that are not common to both set1 and set2
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
# Expected output:
# {40, 50, 30}
set1.intersection_update(set2)
print(set1)
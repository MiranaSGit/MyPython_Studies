# Exercise 1: Below are the two lists convert it into the dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
# Expected output:
# 
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
my_dict = dict(zip(keys, values))
print(my_dict)




# Exercise 2: Merge following two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# Expected output:
# 
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3 = dict1.copy()
for x, y in dict2.items():
    dict3[x] = y
print(dict3)

# Alternative Solution1
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# 
# dict3 = {**dict1, **dict2}
# print(dict3)

# Alternative Solution2
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# 
# dict3 = dict1.copy()
# dict3.update(dict2)
# print(dict3)





# Exercise 3: Access the value of key ‘history’ from the below dict
sampleDict = {
   "class": { 
       "student": {
           "name": "Mike",
           "marks": {
               "physics": 70,
               "history": 80
           }
       }
   }
}
# Expected output:
# 
# 80
print(sampleDict['class']['student']['marks']['history'])






# Exercise 4: Initialize dictionary with default values
# 
employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}
my_dict = {}
for i in employees:
    my_dict[i] = defaults
print(my_dict)

# Alternative Solution
# resDict = dict.fromkeys(employees, defaults)
# print(resDict)
# 
# # Individual data
# print(resDict["Kelly"])







# Exercise 5: Create a new dictionary by extracting the following keys from a below dictionary
# Given dictionary:
sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
keys = ["name", "salary"]
my_dict = {}
for i in keys:
    my_dict[i] = sampleDict[i]
print(my_dict)

# Alternative Solution
# newDict = {k: sampleDict[k] for k in keys}
# print(newDict)






# Exercise 6: Delete set of keys from a dictionary
# Given:
sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
keysToRemove = ["name", "salary"]
for i in keysToRemove:
    sampleDict.pop(i)
print(sampleDict)

# Alternative Solution
# sampleDict = {k: sampleDict[k] for k in sampleDict.keys() - keysToRemove}
# print(sampleDict)





#Exercise 7: Check if a value 200 exists in a dictionary
sampleDict = {'a': 100, 'b': 200, 'c': 300}
if 200 in sampleDict.values()
    print("True")

# or 
# print(200 in sampleDict.values())





# Exercise 8: Rename key city to location in the following dictionary
sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
#Expected output:
# {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "location": "New york"
# }
sampleDict["location"] = sampleDict.pop("city")
print(sampleDict)






# Exercise 9: Get the key of a minimum value from the following dictionary
sampleDict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}
print(min(sampleDict, key=sampleDict.get))






# Exercise 10: Change Brad’s salary to 8500 from a given Python dictionary
sampleDict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 6500}
}
sampleDict['emp3']['salary'] = 8500
print(sampleDict)

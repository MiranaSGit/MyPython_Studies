# Problem Statement
# Write a python code that finds the largest number among the n numbers given by the user as input.
# 
# First, take n from the user, then take n numbers one by one and select-print the largest one.
# 
# It is forbidden to use max() function.
# 
# Indicate which computational thinking concepts have you used.
#Example for user inputs and respective outputs

num = int(input("please enter number of number you will enter: "))
list = []
max = 0
for i in range(1, num + 1):
  list.append((int(input("Please enter the {}. number: ".format(i)))))
for i in list:
  if i > max:
    max = i
  else:
    continue
print("The largest number is : ",max)




# Problem Statement
# Given a list of strings, group anagrams together.
# 
# Example:
# 
# Input:
# 
# ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#     ["ate", "eat", "tea"],
#     ["nat", "tan"],
#     ["bat"]
# ]
# Note: All inputs will be in lowercase. The order of your output does not matter.

list = ["eat", "tea", "tan", "ate", "nat", "bat"]
sorted_list = []
sonuc = []
for i in list:
  if sorted(i) not in sorted_list:
    sorted_list.append(sorted(i))
for a in range(len(sorted_list)):
  sonuc.append([i for i in list if sorted(i) == sorted_list[a]])
print(sonuc)


# Problem Statement
# Given an array of non-negative integers representing an elevation map as shown below 
# where the width of each bar is 1, compute how much water will be trapped on terrain 
# after raining. To clarify further, the black boxes represents terrain and its height, 
# and the blue boxes represents the water that could be trapped on the terrain.
height = []
while True:
    num = input("Type 'ok' when you are done: ")
    if num != "ok":
        height.append(int(num))
    else:
        break
areas = 0
max_l = max_r = 0
l = 0
r = len(height)-1
while l < r:
    if height[l] < height[r]:
        if height[l] > max_l:
            max_l = height[l]
        else:
            areas += max_l - height[l]
        l += 1
    else:
        if height[r] > max_r:
            max_r = height[r]
        else:
            areas += max_r - height[r]
        r -= 1
print("\nRain-trapped area : ", areas)

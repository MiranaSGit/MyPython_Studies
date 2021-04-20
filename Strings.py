# Exercise 1: Given a string of odd length greater than 7, return a new string made of 
# the middle three characters of a given String
text = input("Please provide a text: ")
length = len(text)
if length < 7:
    print("It should be longer than 7 character. Please try again.")
elif length % 2 ==0:
    print("Its lenght should be odd number. Please try again.")
else:
    index = length // 2
    print("The middle characters are {}{}{}".format(
        text[index - 1], (text[index]), (text[index + 1])))


# Exercise 2: Given two strings, s1 and s2, create a new string by appending s2 in the
# middle of s1.
# Given:
s1 = "Ault"
s2 = "Kelly"
# Expected Output:
# AuKellylt
middle = len(s1) // 2
new_str = s1[:middle] + s2 + s1[middle:]
print(new_str)




# Exercise Question 3: Given two strings, s1, and s2 return a new string made
# of the first, middle, and last characters each input string
s1 = "America"
s2 = "Japan"
# Expected Output: AJrpan
middle1 = len(s1) // 2
middle2 = len(s2) // 2
new_str = s1[0] + s2[0] + s1[(middle1)] + \
    s2[(middle2)] + s1[(middle1 * 2)] + s2[(middle2 * 2)]
print(new_str)

# Alternative Solution
# def mix_string(s1, s2):
#     first_char = s1[:1] + s2[:1]
#     middle_char = s1[int(len(s1) / 2):int(len(s1) / 2) + 1] + \
#         s2[int(len(s2) / 2):int(len(s2) / 2) + 1]
#     last_char = s1[len(s1) - 1] + s2[len(s2) - 1]
#     res = first_char + middle_char + last_char
#     print("Mix String is ", res)
# 
# 
# s1 = "America"
# s2 = "Japan"
# mix_string(s1, s2)




# Exercise 4: Arrange string characters such that lowercase letters should come first
# Given an input string with the combination of the lower and upper case
# arrange characters in such a way that all lowercase letters should come first.
str1 = "PyNaTive"
new_str = ""
len = len(str1)
i = 1
# Expected Output: yaivePNT
str1 = "PyNaTive"
lower = []
upper = []
for char in str1:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)
sorted_string = ''.join(lower + upper)
print("arranging characters giving precedence to lowercase letters:")
print(sorted_string)


# Exercise 5: Count all lower case, upper case, digits, and special symbols from a given string
# Given:
str1 = "P@#yn26at^&i5ve"
charCount = 0
digitCount = 0
symbolCount = 0
for char in str1:
   if char.islower() or char.isupper():
     charCount += 1
   elif char.isnumeric():
     digitCount += 1
   else:
     symbolCount += 1
print("Chars = ", charCount, "Digits = ", digitCount, "Symbol = ", symbolCount)





# Exercise 6: Given two strings, s1 and s2, create a mixed String using the following rules
# Note: create a third-string made of the first char of s1 then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.
# s1 = "Abc"
# s2 = "Xyz"
# Expected Output:
# AzbycX
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
s2 = "Xyz"
mixString(s1, s2)




# Exercise 7: String characters balance Test
# We’ll assume that a String s1 and s2 is balanced if all the chars in the s1 
# are there in s2. characters’ position doesn’t matter.
def stringBalanceCheck(s1, s2):
  flag = True
  for char in s1:
    if char in s2:
      continue
    else:
      flag = False
  return flag

s1 = "Yn"
s2 = "PYnative"
flag = stringBalanceCheck(s1, s2)
print("s1 and s2 are balanced", flag)

s1 = "Ynf"
s2 = "PYnative"
flag = stringBalanceCheck(s1, s2)
print("s1 and s2 are balanced", flag)




# Exercise 8: Find all occurrences of “USA” in a given string ignoring the case
# Given:
# str1 = "Welcome to USA. usa awesome, isn't it?"
# Expected Outcome:
# The USA count is : 2
inputString = "Welcome to USA. usa awesome, isn't it?"
substring = "USA"
tempString = inputString.lower()
count = tempString.count(substring.lower())
print("The USA count is:", count)


# Exercise 9: Given a string, return the sum and average of the digits that
# appear in the string, ignoring all other characters
# str1 = "English = 78 Science = 83 Math = 68 History = 65"
# Expected Outcome:
# sum is 294
# average is 73.5

# import re
inputStr = "English = 78 Science = 83 Math = 68 History = 65"
markList = [int(num) for num in re.findall(r'\b\d+\b', inputStr)]
totalMarks = 0
for mark in markList:
  totalMarks += mark

percentage = totalMarks/len(markList)
print("Total Marks is:", totalMarks, "Percentage is ", percentage)

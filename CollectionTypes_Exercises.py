# Exercise 1: Given two lists create a third list by picking an odd-index element from the 
# first list and even index elements from the second.
# Given:
listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
newList = listOne[1::2] + listTwo[::2]
print(newList)




# Exercise 2: Given a list, remove the element at index 4 and add it to the 2nd position
#  and at the end of the list
# Given:
list1 = [54, 44, 27, 79, 91, 41]
# Expected Output:
# Original list[34, 54, 67, 89, 11, 43, 94]
# List After removing element at index 4  [34, 54, 67, 89, 43, 94]
# List after Adding element at index 2  [34, 54, 11, 67, 89, 43, 94]
# List after Adding element at last[34, 54, 11, 67, 89, 43, 94, 11]
item = list1.pop(4)
list1.insert(2, item)
list1.append(item)
print(list1)




# Exercise 3: Given a list slice it into 3 equal chunks and reverse each chunk
# Given:
sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
print("Original list ", sampleList)

length = len(sampleList)
chunkSize = int(length/3)
start = 0
end = chunkSize
for i in range(1, 4, 1):
  indexes = slice(start, end, 1)
  listChunk = sampleList[indexes]
  print("Chunk ", i, listChunk)
  print("After reversing it ", list(reversed(listChunk)))
  start = end
  if(i != 2):
    end += chunkSize
  else:
    end += length - chunkSize

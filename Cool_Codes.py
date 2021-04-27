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

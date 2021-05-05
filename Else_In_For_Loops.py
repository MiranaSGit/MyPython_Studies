for i in range(1, 4):
    print(i)
    break
else:  # Not executed as there is a break
    print("No Break")





def contains_even_number(l):
    for ele in l:
        if ele % 2 == 0:
            print ("list contains an even number")
            break
  
    # This else executes only if break is NEVER
    # reached and loop terminated after all iterations.
    else:     
        print ("list does not contain an even number")
  
# Driver code
print ("For List 1:")
contains_even_number([1, 9, 8])
print (" \nFor List 2:")
contains_even_number([1, 3, 5])





count = 0
while (count < 1):
    count = count+1
    print(count)
    break
else:
    print("No Break")

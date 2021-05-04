# Write a function that given a string containing just the characters 
# (, ), {, }, [ and ], determines if the input string is valid or not 
# by using following rules.
# 
# An input string is valid if:
# 1-Open brackets must be closed by the same type of brackets.
# 2-Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.




def ofd(a):
    dict = {"(" : ")", "[" : "]", "{" : "}"}
    if len(a) == 0:
        return True
    else:
        l_index = 0
        r_index = len(a) - 1
        flag = True
        while flag == True:
            for i in a:
                print(a[r_index])
                print(dict[i])
                if a[r_index] == dict[i]:
                    l_index += 1
                    r_index -= 1
                    print(l_index, r_index)
                    if l_index >= r_index:
                        flag = False
                        break
                else:
                    return False
        return True

t = "{}"
ofd(t)
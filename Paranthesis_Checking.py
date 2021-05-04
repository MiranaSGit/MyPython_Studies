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
                if a[r_index] == dict[i]:
                    l_index += 1
                    r_index -= 1
                    if l_index >= r_index:
                        flag = False
                        break
                else:
                    return False
        return True

t = "{}"
ofd(t)



# Alternative Solution
def is_valid(s):
  parantez = {"(": ")", "[": "]", "{": "}"}
  open_par = set(["(", "[", "{"])
  control_list = []
  for i in s:
    if i in open_par:
      control_list.append(i)
    elif control_list and i == parantez[control_list[-1]]:
      control_list.pop()
    else:
      return False
  return control_list == []

is_valid('[]({}){')

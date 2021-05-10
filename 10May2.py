# Add up all the numbers from 1 to the number you passed to the
# function.
# For example, if the input is 4 then your function should return 10
# because 1 + 2 + 3 + 4 = 10.
def AddUp(num):
    return print(sum([x for x in range(1, num + 1)]))


AddUp(4)
AddUp(13)
AddUp(600)

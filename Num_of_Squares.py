# Calculate number of squares that can be fill in a given rectangle.
# for example 20x7

myDict = {}


def num_of_squares(a, b):
    global myDict

    def compare(x, y):
        myDict[x // y] = str(y)+"x"+str(y)
        c = x - (x//y)*y
        if c != 0:
            if c > y:
                return compare(c, y)
            else:
                return compare(y, c)
    if a > b:
        compare(a, b)
    else:
        compare(b, a)
    return myDict


num_of_squares(20, 7)
print(myDict)

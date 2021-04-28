def fun(a):
    myList = []
    for i in a:
        if i not in myList:
            myList.append(i)
    return myList
print(fun([1, 2, 3, 3, 3, 3, 4, 5]))





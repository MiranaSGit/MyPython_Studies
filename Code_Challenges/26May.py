def array_diff(a, b):
    c = a
    counter = 0
    while counter < len(c):
        for i in c:
            if i in b:
                a.remove(i)
                c = a
                counter = 0
                break
            else:
                counter += 1
    return a


print(array_diff([1, 1, 2, 1, 2, 3, 3, 1, 1, 5, 5, 1, 1, 8], [1]))

def tribonacci(signature, n):
    if n == 0:
        return []
    elif n == 1:
        return [signature[0]]
    elif n == 2:
        return [signature[0], signature[1]]
    elif n == 3:
        return signature
    else:
        myList = signature
        count = len(signature)
        while count < n:
            myList.append(
                sum([myList[count-3], myList[count-2], myList[count-1]]))
            count += 1
    return myList


tribonacci([1, 1, 1], 10)
tribonacci([0, 0, 1], 10)
tribonacci([0, 1, 1], 10)
tribonacci([1, 0, 0], 10)
tribonacci([0, 0, 0], 10)
tribonacci([1, 2, 3], 10)
tribonacci([3, 2, 1], 10)
tribonacci([1, 1, 1], 1)
tribonacci([300, 200, 100], 0)
tribonacci([0.5, 0.5, 0.5], 30)


# Solution2:
def tribonacci(signature, n):
    res = signature[:n]
    for i in range(n - 3):
        res.append(sum(res[-3:]))
    return res

liste = range(1, 4)
result1 = []
perm = 1
for i in range(1, len(liste)+1):
    perm = i * perm
per = int(perm * 0.5)
for i in range(per):
    result1.append([])
for i in range(len(liste)):
    for j in result1:
        j.append(0)
k = 0
for i in liste:
    k += 1
    for j in range(per):
        if k < len(liste):
            result1[j][k] = i
            k += 1
        else:
            k = 0
            result1[j][k] = i
            k += 1
result2 = []
for i in result1:
    result2.append(i[::-1])
if len(liste) <= 1:
    result = liste
else:
    result = result2 + result1
result


# Solution2
nums = "123"
result_perms = [[]]
for n in nums:
    new_perms = []
    for perm in result_perms:
        for i in range(len(perm)+1):
            new_perms.append(perm[:i] + [n] + perm[i:])
            result_perms = new_perms
print(result_perms)

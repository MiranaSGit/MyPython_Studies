print(*range(11), sep="\n")

# Exercise 2: Print the following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
i = j = 1
while i < 6:
    while j <= i:
        print(j)
        j += 1
    i += 1


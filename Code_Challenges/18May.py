# Write a method that takes an array of consecutive(increasing) letters as input and
# that returns the missing letter in the array. You will always get an valid array.
# And it will be always exactly one letter be missing. The length of the array will
# always be at least 2. The array will always contain letters in only one case.

# Example:
# ['a', 'b', 'c', 'd', 'f'] -> 'e'
# ['O', 'Q', 'R', 'S'] -> 'P'
# ["a", "b", "c", "d", "f"] -> "e"
# ["O", "Q", "R", "S"] -> "P"
# (Use the English alphabet with 26 letters!)
def checker(words):
    myList_lower = list('abcdefghijklmnopqrstuvwxyz')
    myList = myList_lower + list(str('abcdefghijklmnopqrstuvwxyz').upper())
    Flag = True
    for i in words:
        if words.index(i) != len(words)-1:
            if words[words.index(i)+1] != myList[myList.index(i) + 1]:
                print(myList[myList.index(i) + 1])
                flag = False
        else:
            if Flag != False:
                print(words)


checker(["d", "e", "f", "g"])


# Sol2
def eksik_b(l):
    new_l = []
    for i in l:
        new_l.append(ord(i))
    return [chr(x) for x in range(new_l[0], new_l[-1]+1) if x not in new_l]


print(eksik_b(['a', 'b', 'c', 'd', 'f']))


# Sol3:
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
     'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def missing_letter(s):
    for letter in s:
        if not l[(l.index(letter))+1] == s[(s.index(letter))+1]:
            return print(l[(l.index(letter))+1])


s1 = ['d', 'e', 'f', 'h', 'i']
s2 = ['H', 'I', 'J', 'L', 'M']
missing_letter(s1)
missing_letter(s2)


# Sol4:
def find_missing_letter(chars):
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    b = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i in chars:
        if i in a:
            z = set(a[a.index(chars[0]):a.index(chars[-1])+1])
        else:
            z = set(b[b.index(chars[0]):b.index(chars[-1])+1])
    chars = set(chars)
    return "".join(z-chars)


# Sol5
def missing_letter(s):
    alfabe = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(s)-1):
        if s[i] in alfabe:
            y = alfabe[alfabe.index(s[i])+1]
            if y == s[i+1]:
                pass
            else:
                return y


# Sol6
def missing(l):
    h = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(*filter(lambda x: x not in l, h[h.index(l[0]):h.index(l[-1])]))


s1 = ['d', 'e', 'f', 'h', 'i']
s2 = ['H', 'I', 'J', 'L', 'M']
missing(s1)
missing(s2)

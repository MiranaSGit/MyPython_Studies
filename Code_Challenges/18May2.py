# Your task is to write the word to number converter. Digits in the number should match letters in the word. Plus generated number should be the smallest possible number you can get.

# Words will contain of maximum 10 distinct letters, but word can be any length, even longer than 10 characters long.
# Number can NOT start with 0
# Same letters share the same digit regardless of case
# For empty string return 0
# Examples:
# "A" -> 1 - OK

# "ABA" -> 353 - WRONG(number is OK, but it's not the smallest number)

# "ABA" -> 333 - WRONG(different letters map to same digits)

# "ABA" -> 357 - WRONG(same letters map to different digits)

def convert(st):
    if st == "":
        return 0
    elif len(st) == 1:
        return st
    else:
        list = []
        for i in st.upper():
            if i not in list:
                list.append(i)
        myDict = {j: i for i, j in enumerate(list[2:], 2)}
        myDict[st[0].upper()] = 1
        myDict[st[1].upper()] = 0
        return int("".join([str(i) for i in [myDict[i] for i in st.upper()]]))


convert("Asabi")

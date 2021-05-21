def likes(names):
    if len(names) == 0:
        a = "no one likes this"
        return a
    elif len(names) == 1:
        return print(names[0], "likes this")
    elif len(names) == 2:
        return print("{} and {} like this".format(names[0], names[1]))
    elif len(names) == 3:
        return print("{}, {} and {} like this".format(names[0], names[1], names[2]))
    else:
        return print("{}, {} and {} others like this".format(names[0], names[1], len(names)-2))


likes([])
likes(['Peter'])
likes(['Jacob', 'Alex'])
likes(['Max', 'John', 'Mark'])
likes(['Alex', 'Jacob', 'Mark', "Josph"])

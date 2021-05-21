# You live in the city of Cartesia where all roads are laid out in a perfect grid.
# You arrived ten minutes too early to an appointment, so you decided to take the
# opportunity to go for a short walk. The city provides its citizens with a Walk
# Generating App on their phones - - everytime you press the button it sends you
# an array of one-letter strings representing directions to walk(eg. ['n', 's', 'w', 'e']).
# You always walk only a single block for each letter(direction) and you know it takes
# you one minute to traverse one city block, so create a function that will return
# true if the walk the app gives you will take you exactly ten minutes(you don't want
# to be early or late!) and will, of course, return you to your starting point. Return
# false otherwise.

# Note: you will always receive a valid array containing a random assortment of direction
# letters('n', 's', 'e', or 'w' only). It will never give you an empty array(that's not a
# walk, that's standing still!).

def is_valid_walk(a):
    myDict = {"n": "s", "s": "n", "w": "e", "e": "w"}
    # myList = a
    count = 0
    if len(a) != 10:
        return False
    else:
        while count < len(a):
            if myDict[a[count]] in a:
                del a[a.index(myDict[a[count]])]
                del a[a.index(a[count])]
            else:
                return False

    if len(a) == 0:
        return True


is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'])
is_valid_walk(['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e'])
is_valid_walk(['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's'])


# Solution2
def isValidWalk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')


# Solution3:
def isValidWalk(walk):
    if len(walk) != 10:
        return False

    x, y = 0, 0

    for direction in walk:
        if direction == 'n':
            y += 1
        elif direction == 's':
            y -= 1
        elif direction == 'e':
            x += 1
        elif direction == 'w':
            x -= 1
        else:
            return False

    return x == 0 and y == 0

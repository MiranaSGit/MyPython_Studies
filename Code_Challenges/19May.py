# This time we want to write calculations using functions and get the results. Let's have a look at some examples:

# seven(times(five()))  # must return 35
# four(plus(nine()))  # must return 13
# eight(minus(three()))  # must return 5
# six(divided_by(two()))  # must return 3
# Requirements:

# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy(divided_by in Ruby and Python)
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Division should be integer division. For example, this should return 2, not 2.666666...:
# eight(divided_by(three()))

def plus(y):
    return lambda x: x + y


def minus(y):
    return lambda x: x - y


def times(y):
    return lambda x: x * y


def divided_by(y):
    return lambda x: x // y


def zero(a=None):
    if a == None:
        return 0
    else:
        return a(0)


def one(a=None):
    if a == None:
        return 1
    else:
        return a(1)


def two(a=None):
    if a == None:
        return 2
    else:
        return a(2)


def three(a=None):
    if a == None:
        return 3
    else:
        return a(3)


def four(a=None):
    if a == None:
        return 4
    else:
        return a(4)


def five(a=None):
    if a == None:
        return 5
    else:
        return a(5)


def six(a=None):
    if a == None:
        return 6
    else:
        return a(6)


def seven(a=None):
    if a == None:
        return 7
    else:
        return a(7)


def eight(a=None):
    if a == None:
        return 8
    else:
        return a(8)


def nine(a=None):
    if a == None:
        return 9
    else:
        return a(9)


seven(times(five()))


# Sol2
def id_(x): return x
def number(x): return lambda f=id_: f(x)


zero, one, two, three, four, five, six, seven, eight, nine = map(
    number, range(10))


def plus(x): return lambda y: y + x
def minus(x): return lambda y: y - x
def times(x): return lambda y: y * x
def divided_by(x): return lambda y: y / x


seven(times(five()))

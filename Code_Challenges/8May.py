# Create a function that returns the simplified version of a fraction.
# Examples
# simplify("4/6") ➞ "2/3"
# simplify("10/11") ➞ "10/11"
# simplify("100/400") ➞ "1/4"
# simplify("8/4") ➞ "2"
# Notes
# A fraction is simplified if there are no common factors(except 1) between
# the numerator and the denominator. For example, 4/6 simplified,
# since 4 and 6 both share 2 as a factor. If improper fractions can be
# transformed into integers, do so in your code(see example  # 4).
def simplify(x, y):
    higher = [x if x > y else y]
    set1 = set([i for i in range(2, x+1) if not x % i])
    set2 = set([i for i in range(2, y+1) if not y % i])
    divisor = sorted([i for i in set1.intersection(set2)])
    # print(divisor)
    # print(set1)
    # print(set2)
    res = [int(x/divisor[-1]), int(y/divisor[-1]) if divisor else [x, y]]
    return print(res)


simplify(4, 6)

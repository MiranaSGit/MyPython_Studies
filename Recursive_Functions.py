houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]

# Each function call represents an elf doing his work

# Example:


def countdown(n):
    print(n)
    if n == 0:
        return             # Terminate recursion
    else:
        countdown(n - 1)   # Recursive call

# sol2:


def countdown(n):
    print(n)
    if n > 0:
        countdown(n - 1)


>> > countdown(5)


# Example:
houses = ["adam", "elen", "henry", "eve"]


def deliver_presents_recursively(houses):
    # Worker elf doing his work
    if len(houses) == 1:
        house = houses[0]
        print("Delivering presents to", house)

    # Manager elf doing his work
    else:
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]

        # Divides his work among two elves
        deliver_presents_recursively(first_half)
        deliver_presents_recursively(second_half)


deliver_presents_recursively(houses)


# Example:
def factorial_recursive(n):
    # Base case: 1! = 1
    if n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial_recursive(n-1)

# Sol2:


def factorial_recursive(n):
    return 1 if n <= 1 else n * factorial_recursive(n - 1)


factorial_recursive(5)


# Example3:
def sum_recursive(current_number, accumulated_sum):
    # Base case
    # Return the final state
    if current_number == 11:
        return accumulated_sum

    # Recursive case
    # Thread the state through the recursive call
    else:
        return sum_recursive(current_number + 1, accumulated_sum + current_number)


# Solution2
# Global mutable state
current_number = 1
accumulated_sum = 0


def sum_recursive():
    global current_number
    global accumulated_sum
    # Base case
    if current_number == 11:
        return accumulated_sum
    # Recursive case
    else:
        accumulated_sum = accumulated_sum + current_number
        current_number = current_number + 1
        return sum_recursive()


# Pass the initial state
>> > sum_recursive(1, 0)
55


# Recursive Data Structures in Python
# Return a new list that is the result of
# adding element to the head (i.e. front) of input_list
def attach_head(element, input_list):
    return [element] + input_list


attach_head(1,                                                  # Will return [1, 46, -31, "hello"]
            attach_head(46,                                     # Will return [46, -31, "hello"]
                        attach_head(-31,                        # Will return [-31, "hello"]
                                    attach_head("hello", []))))


# Example2:
def list_sum_recursive(input_list):
    # Base case
    if input_list == []:
        return 0

    # Recursive case
    # Decompose the original problem into simpler instances of the same problem
    # by making use of the fact that the input is a recursive data structure
    # and can be deﬁned in terms of a smaller version of itself
    else:
        head = input_list[0]
        smaller_list = input_list[1:]
        return head + list_sum_recursive(smaller_list)


list_sum_recursive([1, 2, 3])


# Example:
def count_leaf_items(item_list):
    """Recursively counts and returns the
       number of leaf items in a (potentially
       nested) list.
    """
    count = 0
    for item in item_list:
        if isinstance(item, list):
            count += count_leaf_items(item)
        else:
            count += 1

    return count


count_leaf_items([1, 2, 3, 4])
count_leaf_items([1, [2.1, 2.2], 3])


# Example:
def is_palindrome(word):
    """Return True if word is a palindrome, False if not."""
    if len(word) <= 1:
        return True
    else:
        return word[0] == word[-1] and is_palindrome(word[1:-1])


is_palindrome("")
is_palindrome("a")
is_palindrome("foo")
is_palindrome("racecar")
is_palindrome("troglodyte")
is_palindrome("civic")

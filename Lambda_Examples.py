print((lambda x: x**2)(2))

# takes two int, returns mean of them
print((lambda x, y: (x+y)/2)(3, 5))  


# You can also assign the lambda statement in parentheses 
# to a variable :
average = (lambda x, y: (x+y)/2)(3, 5)
print(average)


# Alternatively, you can assign the lambda function definition 
# to a variable then you can call it
average = lambda x, y: (x+y)/2
print(average(3, 5))


# Lambda within Built-in (map()) Functions-1
iterable = [1, 2, 3, 4, 5]
map(lambda x: x**2, iterable)
result = map(lambda x: x**2, iterable)

print(type(result))  # it's a map type
print(list(result))  # we've converted it to list type to print
print(list(map(lambda x: x**2, iterable)))  # you can print directly


# Note that map() takes each element from iterable objects one by one 
# and in order.
letter1 = ['o', 's', 't', 't']
letter2 = ['n', 'i', 'e', 'w']
letter3 = ['e', 'x', 'n', 'o']
numbers = map(lambda x, y, z: x+y+z, letter1, letter2, letter3)

print(list(numbers))
#Output : ['one', 'six', 'ten', 'two']

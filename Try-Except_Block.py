while True:
    no_one = int(input("The first number please : "))
    no_two = int(input("The second number please : "))
    try:
        division = no_one / no_two  # normal part of the program
    except ZeroDivisionError:
        # executes when division by zero
        print("You can't divide by zero! Try again.")
    else:
        # executes if there is no exception
        print("The result of the division is : ", division)
    finally:
        print("Thanks for using our mini divison calculator! Come again!")
        break  # exits the while loop


# Yes, as you can see the output, by using the keyword Exception, we can display
# the name of the exception type. Consider the other example :
while True:
    no_one = int(input("The first number please : "))
    no_two = int(input("The second number please : "))
    try:
        division = no_one / no_two
        print("The result of the division is : ", division)
        break
    except Exception as e:
        print("Something went wrong...Try again.")
        print("Probably it is because of '{}' error".format(e))
        break


try:
    a = 10
    b = 2
    print("The result of division is :", c)
except Exception as e:
    print("The error message is : ", e)


# you can define as many except blocks as you want, to catch and handle specific exceptions
try:
    x = 2/0
except ZeroDivisionError:
    print('Attempt to divide by zero')
except:
    print('Something else went wrong')


# Since all the built-in exceptions are formed a hierarchical structure, you can use the following
# exception syntaxes. To catch several possibilities, it’d be better to use two or more except blocks
# for different exceptions.
....
except ZeroDivisionError:
    print("You can't divide by zero!!")
except ValueError:
    print("You can only enter numbers consisting of digits, not text!!")


....
except (ValueError, TypeError):
    print("You can only enter numbers consisting of digits, not text!!")


....
except ArithmeticError:
    print("I will also catch OverflowError, FloatingPointError and ZeroDivisionError")


fruits = ["banana", "mango", "pear", "apple", "kiwi", "grape"]
counter = 3
while counter > 0:
    try:
        x = int(input("enter a number: "))
        print(fruits[x])
        break
    except IndexError:
        counter -= 1
        print("Please enter a number between {} and {}. You have {}right left. Try again".format(
            1, len(fruits), counter))
    except ValueError:
        counter -= 1
        print("Enter a numeric value. You have",
              counter, " right left. Try again")
    else:
        print("Congrats! You've entered a valid input.")
        break
    finally:
        print("Our fruits are always fresh.")

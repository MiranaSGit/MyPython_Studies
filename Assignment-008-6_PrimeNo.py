# Task : Print the prime numbers which are between 1 to entered limit number (n).
# 
# You can use a nested for loop.
# Collect all these numbers into a list
# The desired output for n=100 :
# 
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
# 61, 67, 71, 73, 79, 83, 89, 97]
def prime(a):
    if a <= 1:
        return False

    for i in range(2, a):
        if not n % i:
            return False
    return True

# Function to print primes


def printPrime(n):
    for i in range(2, n + 1):
        if isPrime(i):
            print(i, end=" ")


# Driver code
if __name__ == "__main__":
    n = 7
    # function calling
    printPrime(n)

# Alternative Solution 2
def prime_list(l):
    myList = []
    for i in range(1, l + 1):
       # all prime numbers are greater than 1
       if i > 1:
           for j in range(2, i):
               if (i % j) == 0:
                   break
           else:
               myList.append(i)
    return myList


prime_list(11)

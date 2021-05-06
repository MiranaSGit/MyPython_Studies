# Prime Gaps A prime gap of length n is a run of n-1 consecutive composite 
# numbers between two successive primes. See this Resource for more information.
# The prime numbers are not regularly spaced. For example gap between:
# 2 and 3 is 1 3 and 5 is 2 7 and 11 is 4 
# 
# Create a function with following parameters:
# g (integer >= 2) Gap between the consecutive primes
# a (integer > 2) Start of the search (a inclusive)
# b (integer >= a) End of the search (b inclusive) ... and returns the first 
# pair of two prime numbers spaced with a gap of g between the limits a and b.

# prime_gaps(2, 3, 50) ➞ [3, 5]
# Between 2 and 50 we have the following pairs of 2-gaps primes: 3-5, 5-7, 
# 11-13, 17-19, 29-31, 41-43.
# [3, 5] is the first pair between 3 and 50 with a 2-gap. Examples
# prime_gaps(2, 5, 7) ➞ [5, 7]
# prime_gaps(2, 5, 5) ➞ None
# prime_gaps(4, 130, 200) ➞ [163, 167]
# Notes Return None if consecutive prime numbers are not found with the 
# required gap.

def prime_list(g, x, y):
    myList = []
    for i in range(x, y + 1):
       if i > 1:
           for j in range(2, i):
               if i % j == 0:
                   break
           else:
               myList.append(i)
    result = []
    for i in range(len(myList)):
        if (myList[i] - myList[i-1]) == g:
            result.append(myList[i])
            result.append(myList[i-1])
    result2= set(result)
    result = list(result2)
    result.sort()
    return result
prime_list(2, 3, 50)


def prime_mı(a):
  for i in range(2,a):
    prime = True
    for ii in range(2,i):
      if ii==2:
        prime=True
      elif a % ii == 0 :
        prime = False 
  return prime
def gap(x,y,z):
  prime_list=[i for i in range(y,z+1) if prime_mı(i)]
  # sonuc=[[prime_list[i],prime_list[k]] for i in range(len(prime_list)) for k in range(i+1,len(prime_list)) if prime_list[k]-prime_list[i]==x ]      
  # return sonuc[0] if sonuc else None
print(prime_list)

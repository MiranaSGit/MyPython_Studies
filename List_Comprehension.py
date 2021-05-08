fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)


newlist = [x for x in fruits if x != "apple"]


newlist = [x for x in fruits]


newlist = [x for x in range(10)]
print(newlist)


newlist = [x for x in range(10) if x < 5]
print(newlist)


newlist = [x.upper() for x in fruits]
print(newlist)


newlist = ['hello' for x in fruits]
print(newlist)


newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)


# Cool Example
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
  sonuc=[[prime_list[i],prime_list[k]] for i in range(len(prime_list)) \
      for k in range(i+1,len(prime_list)) if prime_list[k]-prime_list[i]==x ]      
  return sonuc[0] if sonuc else None
print(prime_list)

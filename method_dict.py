# dir() fonksiyonu ile sözlüklerin metodlarını alalım
print(dir({}))
"""
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__',
 '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
 '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
 '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__',
 '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__setitem__',
 '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 
 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

bu metodlardan bizim kullanacaklarımız başında ve sonunda "__" karakteri olmayan
lar. Bunları ayıklamak içinde startswith() ya da endswith() kullanabiliriz. 
"""

for method in dir({}):
    if "_" not in method:
        print(method, end = ", ")

"""
Listelerin Metodları:
    
 clear, copy, fromkeys, get, items, keys,
 pop, popitem, setdefault, update, values, 
 
 
 """

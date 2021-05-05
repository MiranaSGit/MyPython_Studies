#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 11:56:28 2021

@author: mtm
"""
# bir veri tipinin hangi metotlara sahip olduğunu görmek için dir() kullanabiliriz
#print(dir(list()))
# yukarıdaki çıktı da bizim işimize yarayacak olanlar başında __ ve sonunda __
# olmayanlar. O halde

for i in dir(list()):
    if not i.startswith("__") and not i.endswith("__"):
        print(i, end = ", ")
    else:
        pass
"""
yukarıda yer alan kodların çıktısı bize şu metodları verir:
    
append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort,
 
   
"""
# append ile başlayalım. listeye öğe ekler. Listenin sonuna ekler
# append ile aynı anda sadece bir öğe eklenir. 
liste = ["elma", "armut", "kiraz"]
liste.append("ayva")
print(liste)



# extend metodu listeye içinde birden fazla öğe barındıran nesnelerin eklenmesi
# için kullanılabilir, Listenin için başka bir listenin öğelerini ekleyelim.

diller = ["arapça", "aramice", "arnavutça", "tarzanca"]
diller_2 = ["ingizlice", "fransızca", "almanca", "Türkçe"]
diller.extend(diller_2)
print(diller)
""" yukarıdaki örnekte diller listesinin içine diller_2 listesinin öğelerini
tek tek eklemiş olduk. append ile sadece tek bir öğe eklerken extend ile iterable
öğeleri olan bir veri tipinin tüm öğelerini ekleyebildik. """

text =  "karakter dizisi"
diller.extend(text)
print(diller)

# insert metodu append ve extend ile listeye öğe eklemeye yarıyor. Fakat bir
# farkla listenin sonuna değil de bizim verdiğimiz index'e öğe ekler. Buraya 
# kadar öğrenmiş olduğumuz tüm metodları kullanarak bir örnek yapalım. 

liste = ["öğe-0", "öğe-1", "öğe-2", "öğe-3", "öğe-4"]
liste.append("öğe-5")
alt_liste = ["öğe-6","öğe-7", "öğe-8"]
liste.extend(alt_liste)
liste.insert(1, "1. indexe eklenen-öğe") # insert ile araya elaman insert ettik
print(liste)

# remove metodunu inceleyelim
# bu metod ile listenin belirtilen öğesini silebiliriz. 
liste.remove("1. indexe eklenen-öğe")  # dikkat!!! index değil değer belirtiyoruz
print(liste)

# reverse bir metot değil fonksiyon. String ve list gibi iterable değerleri
# tersine çevirmek için kullanılır. sonuç olarak bize reversed nesnesi döndürür
ters = reversed(liste)  # Dikkat!!! reversed listenin yapısını değiştirmez.
# bir değişkene atadık. değişkenin tüm öğelerini * ile yazdırdık.
print(*ters)  
# listeleri tersine çevirmek için dilimlime yöntemi kullanılabilir.
print(liste[::-1])
# ayrıca reverse metodu da kullanılabiir (reversed = fonkisyon, reverse = metod)
print("listeyi reverse metodu ile ters çevirelim")
liste.reverse()
print(liste)
# pop metodu bu metod listeden öğe siler. Sildiği öğeyi de ekrana yazdırır. Eğer
# parametre girilmezse en sonda yer alan öğeyi siler. Parametre olarak index numarası
# girilir. 
print(liste.pop(1))

# sort() metodu ile listenin öğreleri belli bir sıraya göre dizilir.
# alfabetik ya da numeric sıralama gözlenir. 
dağınık_liste = ["9", "4", "6", "8", "5", "1", "3", "o", "u", "g", "4"]
dağınık_liste.sort()
print(dağınık_liste)
# listeyi tersden sıralamak istersek reverse = True parametresi girilir
dağınık_liste.sort(reverse=True)
print(dağınık_liste)

# index metodu ile listede yer alan öğenin index numarasını bulalım
print(dağınık_liste.index("6"))

# count() metodu bir öğenin listede kaç defa geçtiğini sayar
print(dağınık_liste.count("4"))

# copy bir listeyi kopyalamak için kullanılır.
düzenli_liste = dağınık_liste.copy()
print(düzenli_liste)

# clear bir listeyi temizlemek yani içini boşaltmak için kullanılır.
düzenli_liste.clear()
print(düzenli_liste)

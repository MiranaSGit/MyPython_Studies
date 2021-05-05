# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 20:41:29 2021

@author: Joseph Forest
"""
şehirler = ["tokyo", "addi ababa" , "rome" ,"istanbuul", "rio"]
print(sorted(şehirler, key = len))


# listenin elemanlarının uzunluğuna göre listeyi sıralamak için key parametresine
#  len fonksiyonun çağırmadık len fonksiyonunu atadık. 

print(sorted(şehirler, key = len, reverse=True))
# yukarıda yer alan kod ile şehirler listemizin öğelerini en uzundan en kısaya
# olacak şekilde yazdırdık. Bunun içinde reverse = True parametresini atadık. 

print(şehirler)  # bu çıktıdan anlaşıldığı üzere sorted() fonkisyonu listelerin
# üzerinde değişiklik yapmıyor. Sadece ekrana istenilen şekilde çıktı vermewyi 
# sağlıyor. Ama listenin yapısı aynı kalıyor. 

# Kalıcı olarak değiştirmek istersek sort() metodunu kaullanmamız gerek.

şehirler.sort(key = len, reverse = True)
print(şehirler)
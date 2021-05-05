# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 00:19:26 2021

@author: Joseph Forest
"""

# önce kümelerin metodlarını liste üreteci yöntemi ile görelim.
# ayıklayalım.
set_methods = [i for i in dir(set()) if not i.startswith("__")]
for i in enumerate(set_methods,1):
    print(i)

# çıktı incelediğimizde toplamda 17 adet metodun işimize yaradığını görüyoruz. 
# (1, 'add')
# (2, 'clear')
# (3, 'copy')
# (4, 'difference')
# (5, 'difference_update')
# (6, 'discard')
# (7, 'intersection')
# (8, 'intersection_update')
# (9, 'isdisjoint')
# (10, 'issubset')
# (11, 'issuperset')
# (12, 'pop')
# (13, 'remove')
# (14, 'symmetric_difference')
# (15, 'symmetric_difference_update')
# (16, 'union')
# (17, 'update')
print("\n\n\n")
########## 1- add() ile başlayalım ##########
# add() anlaşılacağı üzere kümelere üye eklemek için kullanılır. Önce bir boş küme
# oluşturalım. Sonra .add() ile öğeler ekleyelim. Not! öğe eklenebildiğine göre
# kümeler mutable özeliğine sahip. (list, dict,set mutable)
# add ile her defasında sadece bir öğe eklenebilir. add() sadece bir tane argüman alır
küme = set()
küme.add("bir")
küme.add("iki")
# add() aldığı argümanı iterate etmez tek bir öğe gibi ekler.
küme.add((1,2,3,4))  # {(1, 2, 3, 4), 'iki', 'bir'} tuple tek bir öğe
print(küme)
# kümelere sadece immutable veri tipleri eklenebilir.
# küme.add([5,6,7,8])  # unhashable type: 'list' hatasını verir. baştaki # sil.
# eğer kümede zaten olan bir eleman eklemek istersek add() hata vermez ama
# öğeyi de eklemez.
küme.add("bir")  # zaten küme de oldğu için eklemedi
# hatırlatma!!! sözlüklerin de key kısmına sadece immutable tipler verilebilir.

############## 2- clear()  #############
# clear sözlüklerde de olduğu gibi kümenin tüm elemanlarını siler geriye boş
# küme kalır. kümenün kendisini silmez!!!
küme.clear()
print(küme)  # set() çıktısını verir. temizlik yaptık.

############ 3- copy #############
# listelerde ve sözlüklerde de kullandığımız bir metod
# bu metod yardımı ile kopya çekebiliriz :)
# kümenin içini clear() ile temizlemiştik. şimdi yeniden öğe ekleyelim
küme = set(["bir", "iki", "üç", 1, 2, 3])
# Dikkat!!! Küme oluştururken add() metodunda yer alan immutable nesne sadece eklenebilir şartı yok.
# var olan kümeye add() ile mutable öğe ekleyemeyiz!!!
kopya_küme = küme.copy()
print(kopya_küme)

############# 4- differece ##############
# bu metot (metod imla hatası imiş) ile iki kümenin farkını alabiriz.
# iki ve üç ile tam bölünen sayıların kümesini b2 ve b3 şeklinde tanımlayalım
b2 = set(range(0,100,2))
b3 = set(range(0,100,3))
print(b2.difference(b3))  # b2 kümesinde olup b3 kümesinde olmayan elemanlar
# differance yerine print(b2-b3) de kullanbiliriz. " - " ile b3 fark b2 yazdıralım
print(b3 - b2)
print("\n\n")

############# 5- difference_update()  #############
# adından da anlaşılacağı üzere hem bir kümenin diğerinden farkını alıyor ve
# kümenin yapısını farka göre güncelliyor.
# b2 0' dan 98' e kadar çift sayıların olduğu bir kümeydi.
b2.difference_update(b3)  # kümemizi iki kümenin farkına göre güncelledik. 
# kalıcı değişiklik meydana geldi. 
print(b2)

############# 6- discard #############
# discard metotu ile kümelerden eleman silebiliriz. Bu metot silme işlemini
# yaparken; silmek istediğimiz eleman kümede yoksa bile hata vermez. 
kümes = {"tavuk", "ördek", "tavşan", "hindi", "tilki"}
kümes.discard("tilki")  # kümesten tilki sildiik.
kümes.discard("sansar")  # sansar zaten kümede yok ama yine de hata vermedi.
print(kümes)

#############7- intersection #############
# intersection kesişim anlamına gelir. Matematik dersinden hatırladığımız üzere
# kesişim iki kümenin ortak elemanları anlamına gelir. 
# difference metotunda kullandığmız b2 ve b3 kümelerini yeniden tanımlayıp kullanalım.
b2 = set(range(0,101,2)) 
b3 = set(range(0,101,3))
# hem ikiye hem de 3 bölünen sayıları ekrana yazdıralım.
print(b2.intersection(b3)) # kümeler unordered olduğu için çıktı biraz karışık olur.
# eğer istersek sorted fonkiyonu ile ya da listelerin sort metotu ile ordered yapabiliriz.
print(*sorted(b2.intersection(b3)))  # '*' print foksiyonu içinde iterable nesneleri yazdırmak için kullanılır.
# intersection metodu ile aynı işi yapan b2 & b3 yazımı da mevcut. 

############# 8- intersection_update #############◘
# difference --difference_update ikilisinde olduğu gibi 
# intersection_update ile kümeyi kesişim kümesi olarak güncelleyebiliriz.
# yani farklı elemanlar kümeden silinir sadece ortak elemanlar kümede kalır
# şimdi b2 kümesinin elemanlarını sadece b3 kümesinin kesişimi kalacak şekilde
# değiştirelim.
b2.intersection_update(b3)
print(b2)  # b2 kümesini bu şekilde kalıcı olarak değiştirdik.
# Not!!! kesişim = b2.intersection(b3) şeklinde bir atama yaparak. 3. bir küme
# oluşturabiliriz. Bu sayede elimizde var olan kümenin yapısını bozmamış oluruz.

############# 9- isdisjoint ############# 
# bu metot kümeler üzerinde değişiklik yapan metotlardan değil. Bu metot ile 
# sorgulama yapıyoruz. iki kümenin kesişim kümesinin boş küme olup olmadığını 
# sorguluyoruz. Dolayısı ile bu metot bize True ya da False çıktısı verir.
a = set("ankara adana afyon amasya adıyaman".split())  # string ifadeden küme tanımladık
b = {"new york", "london", "addis ababa", "rio", "capetown"}
print(a.isdisjoint(b))  # kesişim boş küme olduğu için True değerini ekrana yazar.
# a ve b kümeleri ayrık kümeler. Yani hiç ortak elemanları yok. 

############# 10- issubset #############
# bu metod yardımı ile bir kümenin başka bir kümenin alt kümesi olup olmadığını
# sorgulayabiliriz. subset zaten alt küme anlamına geliyor. 
# 4 ile bölünen tüm sayılar ile de tam bölünür. 2 ile tam bölünen tüm sayılar
# 4 ile tam bölünemez. yani 4 ile bölünen sayılar kümesi 2 ile bölünen tam sayıların
# alt kümesidir. 100 ile 200 arasında yer alan sayılardan 2 ile ve 4 ile tam bölünen
# sayıların kümesini oluşturalım. sonra alt küme sorgulaması yapalım.
iki_ile_bölünen = set(range(100,200,2))
dört_ile_bölünen = set(range(100,200,4))
print(iki_ile_bölünen.issubset(dört_ile_bölünen))  # False değeri döner. 
print(dört_ile_bölünen.issubset(iki_ile_bölünen))  # True değeri döner
# adana ve adıyaman şehirlerinden küme oluşturup alt küme sorgulaması yapalım.
adana = set("adana")  # kümesinin elemanları: {a,d,n}
adıyaman = set("adıyaman")  # kümesinin elamanları {a,d,ı,y,m,n}
print(adana.issubset(adıyaman))  # adana adıyamanın alt kümesi sonuç True

############# 11- issuperset ############
# eğer a kümesi b kümenin tüm elemanlarını zaten kendi içinde
# barındıyorsa a kümesi b kümesini kapsar. yani a kümesi b kümesinin superset i 
# oluyor. Bunu sorgulamak için issuperset kullanılır. 
print(adıyaman.issuperset(adana))  # adıyaman kümesi adana kümesini kapsar.

############# 12- pop #############
# kümeden rastgele bir eleman siler ve silinen öğeyi ekrana yazdırır. Boş küme
# üzerinde işlem yapmak hata verir. KeyError: 'pop from an empty set'
# https://docs.python.org/3.8/library/stdtypes.html#frozenset.pop resmi döküman

############# 13- remove #############
# discard metodu ile aynı görevi görür. tek fark ise kümeden olmayan elamanı bu
# metot ile silmek istersek hata verir. Keyerror hatası. 

############# 14- symmetric_difference #############
# bir kümenin diğer kümeden farkını difference ile gördük. yani a fark b ya da a-b
# iki kümenin farkının bileşimini almak istersek symmetric_difference işimize yarar.
x = {1,2,3,4}
y = {2,4,6,8}
print(x.symmetric_difference(y))  # iki kümenin farkının bileşimi = {1, 3, 6, 8}
print(y.symmetric_difference(x))  # aynı sonucu verir. iki kümenin farkının bileşimi

############# 15- symmetric_difference_update #############
# iki kümenin farkının birleşiminden dönen veri ile kümenin yapısını değiştirmek
# için kullanılır. 
x.symmetric_difference_update(y) # x kümesini; x ve y kümesinin farklarının bileşimi 
# olacak şekilde değiştirdik.
print(x)

############# 16- union #############
#♣ iki kümenin birleşimini almamıza yarar. a | b şeklinde de yazılabilir.
tür = {"kedi", "keçi", "koyun", "at", "it", "tavuk", "insan"}
yavru = {"manık", "oğlak", "kuzu", "tay", "civciv", "bebek"}
print(tür.union(yavru))
bileşik_küme = tür | yavru
print(bileşik_küme)

############# 17- update #############
# add metotu ile kümeye her seferinde tek eleman eklerken bu metot ile 
# birden fazla elemanı tek seferde ekleyebiliriz. bir şartla update()
# metotuna verdiğimiz argüman iterable olmalı. (liste, tuple,sözlük,string)

a = {"adana", "adıyaman", "afyon", "amasya", "ankara"}  # küme
b = ["bolu", "bursa", "burdur", "bitlis", "bingöl", "bilecik"]  # liste
# a kümesine b listesinin elemanlarını ekleyelim.
a.update(b)     
print(a)



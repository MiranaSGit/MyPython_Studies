# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 23:30:35 2021

@author: Joseph Forest
"""

# Kümeler 'set' matematikteki küme kavramı ile aynı özellikleri taşır.
# kümeler üzerinde fark, kesişim, birleşim gibi işlemleri yapabiliriz.
# Kümelerde her eleman sadece bir kez bulunabilir. bu özelliğe uniqe ya da eşsiz denir.
# boş bir küme sadece set() fonksiyonu ile oluşturulabilir.
# kümelerin öğelerine index ile erişilemez küme[] şeklinde bir erişim yok.
# kümlerde öğelerin index sırası yok. Çünkü öğelerin sabit bir sırası, indexi yok.

# boş bir küme oluşturalım. set() fonkisyonu diğer collection fonksiyonlar ile 
# aynı şekilde/mantıkta çalışır.
boş_küme = set()
print(type(boş_küme))

# diğer collection veri tiplerinden set() fonksiyonu ile birkaç küme tanımlayalım.
set_from_str = set("aaabbbcccddeeffghaagfg")  # her bir karakter bir kere alınacak
print(set_from_str)  # {'g', 'a', 'h', 'f', 'd', 'c', 'e', 'b'}
set_from_list = set([1,2,3,3,2,1,"a","aa","b"])  # {1, 2, 3, 'a', 'b', 'aa'}
print(set_from_list)  # listelerden küme tanımladık.
set_from_tuple = set((True, False, 1, 0, "a", "b", None))
print(set_from_tuple)  # OUTPUT DİKKAT!!!. Açıklama alt satırda
# True, False, 1, 0 değerlerinden sadece biri küme'nin elemanı olabiliyor.
# çünkü kümeler True ile 1 ve False ile 0 ı eşit sayıyor. Sadece birini ekliyor.
# yukarıda set() fonksiyonu ile sadece iterable olan veriler ile küme oluşturulabilir.
# sözlükler ile küme oluşturursak sadece key leri öğe olarak alır
sözlük = dict(book = "kitap", door = "kapı", wall = "duvar", table = "masa")
set_from_dict = set(sözlük)
print(set_from_dict)  # sadece keyler: {'book', 'wall', 'door', 'table'}
# sözlük nesnesinin value leri ile küme yapalım.
set_from_dict_values  = set(sözlük.values())
print(set_from_dict_values)  # {'duvar', 'kapı', 'kitap', 'masa'}
# sözlük nesnesinin itemlerini kullanalım küme yapmak için.
set_from_dict_items = set(sözlük.items())
print(set_from_dict_items)  # output: {('table', 'masa'), ('book', 'kitap'), ('wall', 'duvar'), ('door', 'kapı')}






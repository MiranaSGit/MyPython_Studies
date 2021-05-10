# Verilen cumledeki kelimelerde yer alan rakamlara gore cumleyi
# tekrar olusturan bir fonksiyon yazmak. Cumlenin ilk harfinin
# buyuk olduguna dikkat edelim.

# Cumlede noktalama isaretleri bulunmamaktadir.

# Ornek: string = ‘Bir2 bu1 test4 kolay3’
# Istenen = ‘Bu bir kolay test’

def resolver(string):
    list1 = [x for x in string.split()]
    dict = {}
    res = ""
    for x in list1:
        for j in x:
            if j.isdigit():
                dict[int(j)] = x.replace(j, "")
    for i in range(1, len(dict) + 1):
        res += dict[i] + " "
    print(res.capitalize().strip())


resolver("Bir2 bu1 test4 kolay3")

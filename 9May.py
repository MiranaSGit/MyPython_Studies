# Verilen cumledeki en kisa kelimenin uzunlugunu bulmak
def shortest(sentence):
    return min([len(i) for i in [x for x in sentence.split()]])


print(shortest("Her soru cozumuyle kodlama becerim gelisiyor."))
print(shortest("Bu isi basaririm."))

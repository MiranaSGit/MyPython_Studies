veri = ['a', 'b', True, (False, 1), {'1': 2}, [1, 2], {
    '2': 'two'}, {2, '3'}, 'c', 23, 0]

tipler = ["int", "str", "bool", "list", "tuple", "dict", "set"]
{}.fromkeys(tipler, 0)

toplam = {}.fromkeys(tipler, 0)

for i in range(len(veri)):
    if type(veri[i]) == int:
        toplam["int"] += 1
    elif type(veri[i]) == str:
        toplam["str"] += 1
    elif type(veri[i]) == bool:
        toplam["bool"] += 1
    elif type(veri[i]) == list:
        toplam["list"] += 1
    elif type(veri[i]) == tuple:
        toplam["tuple"] += 1
    elif type(veri[i]) == dict:
        toplam["dict"] += 1
    elif type(veri[i]) == set:
        toplam["set"] += 1

print(toplam)

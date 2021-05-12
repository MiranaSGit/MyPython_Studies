# Verilen = 1.24  istenen = '1 + 2/10 + 4/100'
# Test 1: 70304 = ‘70000 + 300 + 4’
# Test 2: 7.304  istenen = '7 + 3/10 + 4/1000'
# Test 3:  0.04  istenen = '4/100'
def acıkla(n):
    sn = str(n)
    if "." in sn:
        t = sn[:sn.index(".")]
        o = sn[sn.index(".")+1:]
        yeni = "+".join(list(map(str, [int(t[-k])*10**(k-1) for k in range(len(t), 0, -1) if int(t[-k]) != 0]))) \
            + "+" + \
            "+".join([f"{int(o[k])}/{10**(k+1)}" for k in range(0,
                     len(o)) if int(o[k]) != 0])
    else:
        yeni = "+".join(list(map(str, [int(sn[-k])*10**(k-1)
                        for k in range(len(sn), 0, -1) if int(sn[-k]) != 0])))
    return yeni.strip("+")


acıkla(75826.0125)


def genisletilmis_form(num):
    if '.' in str(num):
        tam_sayi, ondalik_sayi = str(num).split('.')
        result = [str(int(num) * (10 ** i))
                  for i, num in enumerate(tam_sayi[::-1]) if num != '0'][::-1]
        result += [str(num) + '/' + str(10 ** (i + 1))
                   for i, num in enumerate(ondalik_sayi) if num != '0']
        return ' + '.join(result)
    else:
        result = [str(int(num) * (10 ** i))
                  for i, num in enumerate(str(num)[::-1]) if num != '0'][::-1]
        return ' + '.join(result)


genisletilmis_form(75826.0125)


number = str(float(input("enter a number: ")))
dot = number.index(".")
text = ""
add = ""
sup = dot
for i in number[:dot]:
    if int(i) == 0:
        sup -= 1
    else:
        text += str(int(i)*(10**(sup-1)))
        if sup != 1:
            text += " + "
        sup -= 1
sup = 1
for i in number[dot+1:]:
    if int(i) == 0:
        sup += 1
    else:
        if sup != len(number[dot+1:])+1:
            text += " + "
        text += i+"/"+str(10**sup)
        sup += 1
print(text)

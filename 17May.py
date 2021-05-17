def navigate(l):
    mydict = {"Kuzey": "Guney", "Guney": "Kuzey",
              "Dogu": "Bati", "Bati": "Dogu"}
    flag = True
    while flag == True:
        if len(l) != 1:
            for i in l:
                if l.index(i) != (len(l)-1):
                    if l[(l.index(i)+1)] == mydict[i]:
                        del l[l.index(i)+1]
                        del l[l.index(i)]
                        break
                else:
                    flag == False
                    return l
        else:
            return l


navigate(["Kuzey", "Bati", "Guney", "Dogu"])

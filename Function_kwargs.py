def couples(bride, groom):
    couple_list = []
    for x in zip(bride, groom):
        couple_list.append(x)
    return couple_list

dict_couple = {"bride": ["mary", "bella", "linda"],
               "groom": ["rye", "fred", "roland"]}
couples(**dict_couple)


# def couples(bride, groom):
#     return [x for x in zip(bride, groom)]


def average(ahmet, hasan, mehmet):
    avg = (ahmet + hasan + mehmet) / 3
    print("The average of their ages is: ", round(avg))

dict_friends = {"ahmet": 22, "hasan": 56, "mehmet": 35}
average(**dict_friends)
average(22, 56, 35)

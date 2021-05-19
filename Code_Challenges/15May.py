def parse_code(word):
    myDict = {}
    a = [i for i in word.split("0") if i != ""]
    myDict["first_name"] = a[0]
    myDict["last_name"] = a[1]
    myDict["id"] = a[2]
    return myDict


parse_code("michael0smith004331")


# Solution2
def parse_code(word):

    return dict(zip([i for i in ("first_name", "last_name", "id")], [j for j in word.split("0") if j != ""]))


parse_code("John000Doe000123")

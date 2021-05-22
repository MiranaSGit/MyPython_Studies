sea = open("Rumi.txt", "r")
print(sea.read(35))
print(sea.read(13))
print(sea.tell())
sea.seek(15)
print(sea.read(20))


sea.seek(0)
print("-------------")
print(sea.readline())
print(sea.readline(13))

print(sea.tell())
sea.seek(0)
print("-------------")
print("-------------")
print(sea.readline())
print(sea.readline())
print(sea.readline(19))

sea.seek(0)
print("-------------")
print("-------------")
print(sea.readlines())
sea.seek(0)

print("-------------")
print("-------------")
print("reading by using for loop")

for line in sea:
    print(line)
sea.close()


for line in sea.readlines():
    print(line)
sea.close()


# With .... As Format #######################
#############################################
# With ... as is used not to use close() function. It closes the file
with open("Rumi.txt", "r") as sea:
    print(sea.read(33))               # automatically.
    print(sea.read(33))
    sea.seek(0)
    print(sea.read(33))
    print(sea.tell)

# Creating A New File:
# As "w" parameter used, it overwrites:
with open("Dosyam.txt", "w", encoding="utf8") as dosyam:
    dosyam.write("Bu benim ilk satirim")

with open("Dosyam.txt", "w", encoding="utf8") as dosyam:
    dosyam.write("Bu benim ilk satirim. ama aslında ikinci satirim.")

with open("Dosyam.txt", "w", encoding="utf8") as dosyam:
    dosyam.write(
        "Bu benim ilk satirim.\n ama aslında ikinci satirim.\nBu da benim ucuncu satirim.")

with open("Dosyam.txt", "r") as dosyam:
    print(dosyam.readline())


fruits = ["Banana", "Orange", "Apple", "Strawberry", "Cherry"]
with open("furits.txt", "w", encoding="utf-8") as file:
    for meyve in fruits:
        file.write(meyve + "\n")
with open("furits.txt", "r") as file:
    print(file.readlines())

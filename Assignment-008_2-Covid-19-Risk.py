# Problem :
# Task: Estimating the risk of death from coronavirus. Write a program that
# 
# Takes "Yes" or "No" from the user as an answer to the following questions:
# 
# Are you a cigarette addict older than 75 years old? Variable → age
# 
# Do you have a severe chronic disease? Variable → chronic
# 
# Is your immune system too weak? Variable → immune
# 
# Set a logical algorithm using boolean logic operators ( and / or ) and use if-statements with 
# the given variables in order to print out us a message : "You are in risky group"(if True ) or 
# "You are not in risky group" (if False).

# age = False  
# chronic = False  
# immune = False
myDict = {} 
while True:
    myDict["age"] = input("Are you a cigarette addict older than 75 years old? Yes or No: ").lower().strip()
    myDict["chronic"] = input("Do you have a severe chronic disease? Yes or No: ").lower().strip()
    myDict["immune"] = input("Is your immune system too weak? Yes or No: ").lower().strip()
    for i, j in myDict.items():
        if j == "yes":
            myDict[i] = True
        else:
            myDict[i] = False
    risk = myDict["age"] or myDict["chronic"] or myDict["immune"]
    if risk == True:
        print("You are in risky group")
    else:
        print("You are not in risky group")
    break


from random import choice
path = ['Data Science', 'DevOps/AWS', 'Full Stack']
ch = []
count = 0
while count < 100:
    ch.append(choice(path))
    count += 1
DS_say = []
DO_say = []
FS_say = []
for i in ch:
    if i == 'Data Science':
        DS_say.append(i)
    elif i == 'DevOps/AWS':
        DO_say.append(i)
    else:
        FS_say.append(i)

DataScience = " % " + str(len(DS_say)) + " Your Path is " + "DataScience"
DevOpsAWS = " % " + str(len(DO_say)) + " Your Path is " + "DevOpsAWS"
FullStack = " % " + str(len(FS_say)) + " Your Path is " + "FullStack"
print(
    f' Canguralations and reinvent yourself. ******\
    {max(DataScience, DevOpsAWS, FullStack)}******')

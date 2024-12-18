with open("input.txt","r") as file:
        list = file.readlines()
for i in range(len(list)):
    item = list[i]
    list[i] = item.split()
newList = []
for row in list:
    for element in row:
        newList.append(element)

leftSide = []
rightSide = []
for i in range(len(newList)):
    if i%2==0:
        leftSide.append(int(newList[i]))
    else:
        rightSide.append(int(newList[i]))
sampleLeft = [3,4,2,1,3,3]
sampleRight = [4,3,5,3,9,3]
total = 0
for i in range(len(leftSide)):
    lMin = leftSide[0]
    for i in range(len(leftSide)):
        if leftSide[i]<lMin:
            lMin = leftSide[i]

    rMin = rightSide[0]
    for i in range(len(rightSide)):
        if rightSide[i]<rMin:
            rMin = rightSide[i]

    distance = abs(lMin-rMin)
    total = distance + total
    leftSide.remove(lMin)
    rightSide.remove(rMin)
print(total)

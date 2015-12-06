import re

toggleRE = re.compile("toggle")
turnoffRE = re.compile("turn off")
turnonRE = re.compile("turn on")
cordsRE = re.compile("\d+")
squareSize = 1000

def turnOn(num):
    return num +1
def turnOff(num):
    if num == 0:
        return num
    return num -1
def toggle(num):
    return num + 2


lightArray = [[0 for i in range(squareSize)] for j in range(squareSize)]

with open('Day06/LightDirections.txt') as file:
    while True:
        line = file.readline().rstrip()
        if not line:
            break

        action = turnOn
        if(toggleRE.match(line)):
            action = toggle
        elif(turnoffRE.match(line)):
            action = turnOff

        cords = cordsRE.findall(line)
        for x in range(int(cords[0]),int(cords[2])+1):
            for y in range(int(cords[1]),int(cords[3])+1):

                lightArray[x][y] = action(lightArray[x][y])

output = open("lightArray.txt","w")


finalOnCount = 0
for x in range(squareSize):
    output.write(lightArray[x].__str__())
    finalOnCount = finalOnCount + sum(lightArray[x])
print (finalOnCount)

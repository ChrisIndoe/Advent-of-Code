import math
import re
regx = re.compile("(\w+)\D+(\d+)\D+(\d+)\D+(\d+)")
Time = 2503
furthest = 0
raindeers = []

def flightDistance(line, time):
    vals = regx.findall(line)[0]
    name = vals[0]
    speed = int(vals[1])
    flightTime =  int(vals[2])
    restTime =  int(vals[3])
    loopTime = flightTime + restTime

    loopCount = math.floor(time/loopTime)
    remainingTime = time - (loopCount * loopTime)
    if remainingTime > flightTime:
        return (loopCount + 1) * speed * flightTime
    else:
        return (loopCount) * speed * flightTime + (remainingTime * speed)

class raindeer(object):
    def flightDistance(self, time):
            loopCount = math.floor(time/self.loopTime)
            remainingTime = time - (loopCount * self.loopTime)
            if remainingTime > self.flightTime:
                return (loopCount + 1) * self.speed * self.flightTime
            else:
                return (loopCount) * self.speed * self.flightTime + (remainingTime * self.speed)

    def __init__(self, line):
            vals = regx.findall(line)[0]
            self.name = vals[0]
            self.speed = int(vals[1])
            self.flightTime =  int(vals[2])
            self.restTime =  int(vals[3])
            self.loopTime = self.flightTime + self.restTime
            self.points = 0
            return
    def addPoint(self):
        self.points = self.points + 1

with open('Day14/Speeds.txt') as file:
    while True:
        line = file.readline().rstrip()
        if not line:
            break
        raindeers.append(raindeer(line))

for second in range(1,(250+1)):
    curPos = []
    for deer in raindeers:
        curPos.append(deer.flightDistance(second))
    leadDist = max(curPos)

    for (i,pos) in enumerate(curPos):
        if pos == leadDist:
            raindeers[i].addPoint()

for deer in raindeers:
    print(deer.name, deer.points)

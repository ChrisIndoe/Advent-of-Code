class location:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return other and self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__0(other)

    def moveUp(self):
        return location(self.x, self.y+1)

    def moveDown(self):
        return location(self.x, self.y-1)

    def moveRight(self):
        return location(self.x+1, self.y)

    def moveLeft(self):
        return location(self.x-1, self.y)

    def __str__(self):
        return "{0},{1}".format(self.x, self.y)
    def __repr__(self):
        return self.__str__()

startingLocation = location(0,0)
currentLocationSanta = startingLocation
currentLocationRoboSanta = startingLocation
locationHistory = {startingLocation:2}

moveRoboSanta = False

with open('Day03/elfDirections.txt') as file:

    while True:
        character = file.read(1)

        if(moveRoboSanta):
            currentLocation = currentLocationRoboSanta
        else:
            currentLocation = currentLocationSanta

        if not character:
            break
        if character == '^':
            currentLocation = currentLocation.moveUp()
        if character == 'v':
            currentLocation = currentLocation.moveDown()
        if character == '>':
            currentLocation = currentLocation.moveRight()
        if character == '<':
            currentLocation = currentLocation.moveLeft()

        locationHistory[currentLocation] = locationHistory[currentLocation] + 1 if currentLocation in locationHistory else 1

        if(moveRoboSanta):
            currentLocationRoboSanta = currentLocation
        else:
            currentLocationSanta = currentLocation

        moveRoboSanta = not moveRoboSanta
        print(currentLocationSanta.x,",",currentLocationSanta.y, "--",currentLocationRoboSanta.x,currentLocationRoboSanta.y)

print("Ending location:", currentLocation.x, currentLocation.y)

locationsWithMultipleVisits = []
locationsWithMultipleVisitsCount = 0
for (location,visits) in locationHistory.items():
    if visits > 0 and not location in locationsWithMultipleVisits:
        locationsWithMultipleVisits.append(location)
        locationsWithMultipleVisitsCount = locationsWithMultipleVisitsCount +1
print("Locations With Mulitiple Visits:", locationsWithMultipleVisitsCount)

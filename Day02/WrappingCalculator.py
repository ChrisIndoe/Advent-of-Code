class Box:
    def __init__(self, length, width, height):
        self.length = int(length)
        self.width = int(width)
        self.height = int(height)

        self.sideLW = self.length * self.width
        self.sideWH = self.width * self.height
        self.sideLH = self.length * self.height

        self.shortSide = min(self.sideLW, self.sideLH, self.sideWH)
        self.surfaceArea = 2*(self.sideLW + self.sideLH + self.sideWH)
        self.wrappingPaper = self.surfaceArea + self.shortSide

        self.maxDim = max(self.length, self.width, self.height)
        self.ribbenAround = 2*(self.length + self.width + self.height - self.maxDim)
        self.bowSize = self.length * self.width * self.height
        self.totalRibben = self.ribbenAround + self.bowSize

box1=Box(2,3,4)

# print("----- Box 1 Test -----")
# print("wrappingPaper: 58 = ", box1.wrappingPaper)
# print("ribben: 34 =", box1.totalRibben)
#
# box2 = Box(1,1,10)
# print("----- Box 2 Test -----")
# print("wrappingPaper: 43 =", box2.wrappingPaper)
# print("ribben: 14 =", box2.totalRibben)

with open('Day 02/Present List.txt') as file:
    WrappingPaperCount = 0
    RibbenCount = 0
    while True:


        line = file.readline().rstrip()
        if not line:
            break

        dims = line.split('x')
        box = Box(dims[0],dims[1],dims[2])
        WrappingPaperCount += box.wrappingPaper
        RibbenCount += box.totalRibben

    print("Total Wrapping Paper:", WrappingPaperCount)
    print("Toatl Ribben", RibbenCount)

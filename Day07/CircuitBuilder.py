import re

def calcValue(a, nul):
    return int(a)

def calcAnd(a,b):
    return a & b
def calcOr(a,b):
    return a | b
def calcLshift( a, num):
    return a << num
def calcRshift( a, num):
    return (a >> num)
def calcNot( a, nul):
    return 65535 - a


circuitDict = {'':''}
wordsRE = re.compile("\S+")

class circuitInstruction(object):

    def val(self):
        try:
            aVal = int(self.a)
        except:
            aVal = circuitDict[self.a]

        if isinstance( aVal, circuitInstruction ):
            aValue = aVal.val()
            circuitDict[self.a] = aValue
            return self.val()

        try:
            bVal = int(self.b)
        except:
            bVal = circuitDict[self.b]

        if isinstance( bVal, circuitInstruction ):
            bValue = bVal.val()
            circuitDict[self.b] = bValue
            return self.val()


        theResult = self.calc(aVal, bVal)

        return theResult

    def __init__(self, instruciton):
        words = wordsRE.findall(instruciton)
        if "NOT" in words:
            self.calc = calcNot
            self.a = words[1]
            self.b = ""
            self.name = words[3]
        elif "AND" in words:
            self.calc = calcAnd
            self.a = words[0]
            self.b = words[2]
            self.name = words[4]
        elif "OR" in words:
            self.calc = calcOr
            self.a = words[0]
            self.b = words[2]
            self.name = words[4]
        elif "RSHIFT" in words:
            self.calc = calcRshift
            self.a = words[0]
            self.b = words[2]
            self.name = words[4]
        elif "LSHIFT" in words:
            self.calc = calcLshift
            self.a = words[0]
            self.b = words[2]
            self.name = words[4]
        else:
            self.calc = calcValue
            self.a = words[0]
            self.b = ""
            self.name = words[2]


        circuitDict[self.name] = self
        return


with open('Day07/CircuitInstructions.txt') as file:
    while True:
        line = file.readline().rstrip()
        if not line:
            break
        circuitInstruction(line)

originalA = circuitDict["a"].val()


with open('Day07/CircuitInstructions.txt') as file:
    while True:
        line = file.readline().rstrip()
        if not line:
            break
        circuitInstruction(line)
circuitDict["b"] = originalA
newA = circuitDict["a"].val()

print ("OringinalA:",originalA)
print("NewA:", newA)

import ast
def rawStringSize(string):
    return len(string)

def calcStringSize(string):
    return len(ast.literal_eval(string))

def calcEncodeSize(string):
    return rawStringSize(string) + string.count('\\') + string.count('\"') + 2

representationSize = 0
actualSize = 0
recodeSize = 0
with open('Day08/InputStrings.txt') as file:
    while True:
        line = file.readline().rstrip()
        if not line:
            break
        representationSize = representationSize + rawStringSize(line)
        actualSize = actualSize + calcStringSize(line)
        recodeSize = recodeSize + calcEncodeSize(line)

print(representationSize, "-", actualSize, "=", representationSize - actualSize)
print(recodeSize, "-", representationSize, "=", recodeSize - representationSize)

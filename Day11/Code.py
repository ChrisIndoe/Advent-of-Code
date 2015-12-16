start = "vzbxkghb"
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', '']

def securityCheck(string):
    prevChar = ''
    prevprevChar = ''
    LetterPairs = 0
    containsConsec = False
    for c in string:
        if c == prevChar and not prevChar == prevprevChar:
            LetterPairs = LetterPairs+1
        if letters.index(c) == letters.index(prevChar)+1 and letters.index(prevChar) == (letters.index(prevprevChar) + 1):
            containsConsec = True
        if c == 'i' or c == 'o' or c == 'l':
            return False
        prevprevChar = prevChar
        prevChar = c
    return containsConsec and LetterPairs > 1

def incrementChar(string):
    modifyStr = list(string[::-1])
    charToModify = 0
    while True:
        if modifyStr[charToModify] == 'z':
            modifyStr[charToModify] = 'a'
            charToModify = charToModify + 1
        else:
            modifyStr[charToModify] = letters[letters.index(modifyStr[charToModify])+1]
            return "".join(modifyStr[::-1])

answerFound = False

while not answerFound:
    start = incrementChar(start)
    answerFound = securityCheck(start)
print (start)
answerFound = False
while not answerFound:
    start = incrementChar(start)
    answerFound = securityCheck(start)
print (start)

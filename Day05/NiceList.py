def has3Vowels(string):
    count = string.count("a") + string.count("e") + string.count("i") + string.count("o") + string.count("u")
    return count > 2

def hasDoubleLetter(string):
    oldLtr = '*'
    for c in string:
        if c == oldLtr:
            return True
        oldLtr = c
    return False

def containsNaughtyStrings(string):
    if "ab" in string:
        return True
    if "cd" in string:
        return True
    if "pq" in string:
        return True
    if "xy" in string:
        return True

def hasLetterSandwich(string):
    oldLtr = '*'
    middleLtr = '*'
    for c in string:
        if c == oldLtr:
            return True
        oldLtr = middleLtr
        middleLtr = c
    return False

def hasMatchingPair(string):
    oldLtr = '*'
    letterPairs = []
    oldPair = ''
    newPair = ''
    for c in string:
        newPair = oldLtr + c
        if newPair in letterPairs:
            return True
        letterPairs.append(oldPair)
        oldPair = newPair
        oldLtr = c
    return False

def isNice(string):
    return has3Vowels(string) and hasDoubleLetter(string) and not containsNaughtyStrings(string)

def isNewNice(string):
    return hasMatchingPair(string) and hasLetterSandwich(string)


print(isNewNice('ieodomaaaucvgmuy'))

with open('Day05/NaughtyOrNice.txt') as file:
    NaughtyList = []
    NiceList = []
    NewNice = []
    NewNaughty = []
    while True:
        line = file.readline().rstrip()
        if not line:
            break
        if isNice(line):
            NiceList.append(line)
        else:
            NaughtyList.append(line)

        if isNewNice(line):
            NewNice.append(line)
        else:
            NewNaughty.append(line)
    print(len(NiceList))
    print(len(NaughtyList))

    print(len(NewNice))
    print(len(NewNaughty))

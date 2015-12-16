import sys
import itertools
from itertools import permutations
from collections import defaultdict

import re
wordsRE = re.compile("\w+")

guests = set()
preferences = dict()

with open('Day13/SeatingPrefs.txt') as file:
    while True:
        line = file.readline().rstrip()
        if not line:
            break

        words = wordsRE.findall(line)
        guests.add(words[0])
        guests.add(words[10])
        happinessValue = int(words[3])
        if words[2] == "lose":
            happinessValue = happinessValue * -1
        preferences.setdefault(words[0], dict())[words[10]] = happinessValue

for guest in guests:
    preferences.setdefault("me", dict())[guest] = 0
    preferences.setdefault(guest, dict())["me"] = 0
guests.add("me")

minHappiness = sys.maxsize
maxHappiness = 0

for arrangement in permutations(guests):
    tableSize = len(arrangement)
    currHappiness = 0
    for i,guest in enumerate(arrangement):
        toRight = arrangement[(i-1) % tableSize]
        toLeft = arrangement[(i+1) % tableSize]

        currHappiness = currHappiness + preferences[guest][toRight]
        currHappiness = currHappiness + preferences[guest][toLeft]

    if currHappiness < minHappiness:
        minHappiness = currHappiness
    if currHappiness > maxHappiness:
        print(arrangement)
        maxHappiness = currHappiness
print(minHappiness,maxHappiness)

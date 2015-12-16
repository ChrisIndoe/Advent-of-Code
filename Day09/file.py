import sys
import itertools
from itertools import permutations
from collections import defaultdict

import re
wordsRE = re.compile("\S+")

locations = set()
distances = dict()

with open('Day09/input.txt') as file:
    while True:
        line = file.readline().rstrip()
        if not line:
            break

        words = wordsRE.findall(line)
        locations.add(words[0])
        locations.add(words[2])
        distances.setdefault(words[0], dict())[words[2]] = int(words[4])
        distances.setdefault(words[2], dict())[words[0]] = int(words[4])

shortestDist = sys.maxsize
longestDist = 0

for item in permutations(locations):
    currDist = 0
    currLoc = item[0]
    for newLoc in item[1:]:
        currDist = currDist + distances[currLoc][newLoc]
        currLoc = newLoc
    if currDist < shortestDist:
        shortestDist = currDist
    if currDist > longestDist:
        longestDist = currDist
print(shortestDist,longestDist)

import json


def recorse(obj):
    if type(obj) == type(dict()):
        if "red" in obj.values():
            return 0
        return sum(map(recorse, obj.values()))

    if type(obj) == type(list()):
        return sum(map(recorse, obj))

    if type(obj) == type(0):
        return obj

    return 0

data = json.loads(open('Day12\logbook.txt', 'r').readline().rstrip())
print(recorse(data))

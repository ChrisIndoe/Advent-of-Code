import fileinput

floor = 0
charIndex = 0
enteredBasement = False
with open('Day01/SantaMap.txt') as file:

    while True:
        charIndex +=1
        character = file.read(1)

        if not character:
            break
        if character == '(':
            floor += 1
        elif character == ')':
            floor -= 1

        if floor == -1 and not enteredBasement:
            enteredBasement = True
            print("Enters Basement at instruction:",charIndex)

    print("Ending  Floor:", floor)

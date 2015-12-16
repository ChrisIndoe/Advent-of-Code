import itertools
import re
reg = re.compile("(\w+): capacity (-?\d), durability (-?\d), flavor (-?\d), texture (-?\d), calories (-?\d)")

class ingredient(object):
    def __init__(self, line):
        matches = reg.findall(line)[0]
        self.name = matches[0]
        self.capacity = int(matches[1])
        self.durability = int(matches[2])
        self.flavor = int(matches[3])
        self.texture = int(matches[4])
        self.calories = int(matches[5])


ingredients = []

with open('Day15/ingredients.txt') as file:
    while True:
        line = file.readline().rstrip()
        if not line:
            break
        ingredients.append(ingredient(line))

maxTaste = 0
bestTaste = []
perms = itertools.permutations(range(1,100),4)
count = 0
for recipe in perms:
    if(sum(recipe) == 100):
        capacity = ingredients[0].capacity * recipe[0] + ingredients[1].capacity * recipe[1] + ingredients[2].capacity * recipe[2] + ingredients[3].capacity * recipe[3]
        durability = ingredients[0].durability * recipe[0] + ingredients[1].durability * recipe[1] + ingredients[2].durability * recipe[2] + ingredients[3].durability * recipe[3]
        flavor = ingredients[0].flavor * recipe[0] + ingredients[1].flavor * recipe[1] + ingredients[2].flavor * recipe[2] + ingredients[3].flavor * recipe[3]
        texture = ingredients[0].texture * recipe[0] + ingredients[1].texture * recipe[1] + ingredients[2].texture * recipe[2] + ingredients[3].texture * recipe[3]
        calories = ingredients[0].calories * recipe[0] + ingredients[1].calories * recipe[1] + ingredients[2].calories * recipe[2] + ingredients[3].calories * recipe[3]
        if capacity > 0 and durability > 0 and flavor > 0 and texture > 0 and calories == 500:
            taste =  capacity * durability * flavor * texture
            maxTaste = max(maxTaste, taste)

print(maxTaste)

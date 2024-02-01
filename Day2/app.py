import os
import time

start = time.time()

def getCubes(round: str):
    red = 0
    blue = 0
    green = 0

    for cube in round.split(','):
        cube = cube.strip()
        if cube.endswith('red'):
            red += int(cube.replace(' red', ''))
        if cube.endswith('blue'):
            blue += int(cube.replace(' blue', ''))
        if cube.endswith('green'):
            green += int(cube.replace(' green', ''))

    return red, blue, green

def posibillity(game: str):
    roundes = game.split(':')[-1].split(';')
    for round in roundes:
        red, blue, green = getCubes(round)
        if red > 12:
            return False
        
        if blue > 14:
            return False
        
        if green > 13:
            return False
    
    return True

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    sum = 0
    for index, game in enumerate(file.readlines()):
        id = index + 1
        if posibillity(game.strip()):
            sum += id

    print(sum)

end = time.time()

print(end - start)
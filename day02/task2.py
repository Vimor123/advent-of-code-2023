games = []

input_file = open("input.txt", "r")

for line in input_file:
    useful_line = line.strip()[line.find(":") + 1:]
    subgames = useful_line.split(";")
    
    game = []
    for subgame_string in subgames:
        subgame = {
            "red" : 0,
            "green" : 0,
            "blue" : 0
        }

        cube_count_strings = subgame_string.strip().split(",")
        for cube_count_string in cube_count_strings:
            no_of_cubes, color = map(str, cube_count_string.split())
            subgame[color] += int(no_of_cubes)
        
        game.append(subgame)

    games.append(game)

input_file.close()

s = 0

for game in games:
    min_cubes = {
        "red" : 0,
        "green" : 0,
        "blue" : 0
    }

    for subgame in game:
        for color, no_of_cubes in subgame.items():
            if min_cubes[color] < no_of_cubes:
                min_cubes[color] = no_of_cubes

    power = 1
    for value in min_cubes.values():
        power *= value

    s += power

print(s)

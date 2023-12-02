limit = {
    "red" : 12,
    "green" : 13,
    "blue" : 14
}

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

for game_index, game in enumerate(games):
    game_valid = True
    for subgame in game:
        for color in limit:
            if subgame[color] > limit[color]:
                game_valid = False
                break
        if not game_valid:
            break

    if game_valid:
        s += game_index + 1

print(s)

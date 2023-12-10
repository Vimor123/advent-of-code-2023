import sys

tile_map = []
starting_position = (-1, -1)

input_file = open("input.txt", "r")

for index, line in enumerate(input_file):
    tile_map.append(line.strip())
    if "S" in line:
        starting_position = (index, line.index("S"))

true_history = []

for starting_move in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
    valid_move = False
    if starting_move == (0, -1):
        if starting_position[1] > 0 and tile_map[starting_position[0] + starting_move[0]][starting_position[1] + starting_move[1]] in ["-", "L", "F"]:
            valid_move = True
    elif starting_move == (-1, 0):
        if starting_position[0] > 0 and tile_map[starting_position[0] + starting_move[0]][starting_position[1] + starting_move[1]] in ["|", "7", "F"]:
            valid_move = True
    elif starting_move == (0, 1):
        if starting_position[1] < len(tile_map[starting_position[0]]) - 1 and tile_map[starting_position[0] + starting_move[0]][starting_position[1] + starting_move[1]] in ["-", "J", "7"]:
            valid_move = True
    elif starting_move == (1, 0):
        if starting_position[0] < len(tile_map) - 1 and tile_map[starting_position[0] + starting_move[0]][starting_position[1] + starting_move[1]] in ["L", "J", "|"]:
            valid_move = True

    if not valid_move:
        continue

    move = starting_move
    history = []
    current_position = [starting_position[0], starting_position[1]]
    loop_reached = False
    move_available = True

    while not loop_reached and move_available:
        history.append(current_position.copy())
        current_position[0] += move[0]
        current_position[1] += move[1]

        next_move_tile = tile_map[current_position[0]][current_position[1]]
        if next_move_tile == "S":
            loop_reached = True
            break
        
        move_available = False

        if move == (0, -1) and next_move_tile in ["-", "L", "F"]:
            if next_move_tile == "-":
                next_move = (0, -1)
            elif next_move_tile == "L":
                next_move = (-1, 0)
            else:
                next_move = (1, 0)
            move_available = True

        elif move == (-1, 0) and next_move_tile in ["|", "7", "F"]:
            if next_move_tile == "|":
                next_move = (-1, 0)
            elif next_move_tile == "7":
                next_move = (0, -1)
            else:
                next_move = (0, 1)
            move_available = True

        elif move == (0, 1) and next_move_tile in ["-", "J", "7"]:
            if next_move_tile == "-":
                next_move = (0, 1)
            elif next_move_tile == "J":
                next_move = (-1, 0)
            else:
                next_move = (1, 0)
            move_available = True

        elif move == (1, 0) and next_move_tile in ["L", "J", "|"]:
            if next_move_tile == "L":
                next_move = (0, 1)
            elif next_move_tile == "J":
                next_move = (0, -1)
            else:
                next_move = (1, 0)
            move_available = True

        if not move_available:
            print("Error2")

        move_available = False

        if current_position[0] + next_move[0] >= 0 and current_position[0] + next_move[0] < len(tile_map) and current_position[1] + next_move[1] >= 0 and current_position[1] + next_move[1] < len(tile_map[current_position[0]]):
            move_available = True

        if not move_available:
            print("Error1")

        move = next_move

    if loop_reached:
        true_history = history.copy()
        break

"""
walled_tile_map = []
for row in tile_map:
    walled_tile_map.append(["."] * len(row))

for position in true_history:
    walled_tile_map[position[0]][position[1]] = "#"
"""

sys.setrecursionlimit(100000)

def spread_darkness(walled_tile_map, position):
    if position[0] < 0 or position[0] >= len(walled_tile_map) or position[1] < 0 or position[1] >= len(walled_tile_map[0]):
        return walled_tile_map
    if walled_tile_map[position[0]][position[1]] == ".":
        walled_tile_map[position[0]][position[1]] = "#"
        for move in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            if position[0] + move[0] >= 0 and position[0] + move[0] < len(walled_tile_map) and position[1] + move[1] >= 0 and position[1] + move[1] < len(walled_tile_map[0]):
                walled_tile_map = spread_darkness(walled_tile_map, [position[0] + move[0], position[1] + move[1]])
    return walled_tile_map

"""
upper_limit = 0
for row in walled_tile_map:
    for character in row:
        if character == ".":
            upper_limit += 1

"""

walled_tile_map_1 = []
walled_tile_map_2 = []
for ri, row in enumerate(tile_map):
    walled_tile_map_1.append([])
    walled_tile_map_2.append([])
    for ci, character in enumerate(row):
        if [ri, ci] in true_history:
            walled_tile_map_1[-1].append(character)
            walled_tile_map_2[-1].append(character)
        else:
            walled_tile_map_1[-1].append(".")
            walled_tile_map_2[-1].append(".")

for i in range(1, len(true_history)):
    move = (true_history[i][0] - true_history[i - 1][0], true_history[i][1] - true_history[i - 1][1])
    if move == (0, -1):
        walled_tile_map_1 = spread_darkness(walled_tile_map_1, [true_history[i - 1][0] + 1, true_history[i - 1][1]])
        walled_tile_map_1 = spread_darkness(walled_tile_map_1, [true_history[i][0] + 1, true_history[i][1]])
    elif move == (-1, 0):
        walled_tile_map_1 = spread_darkness(walled_tile_map_1, [true_history[i - 1][0], true_history[i - 1][1] - 1])
        walled_tile_map_1 = spread_darkness(walled_tile_map_1, [true_history[i][0], true_history[i][1] - 1])
    elif move == (0, 1):
        walled_tile_map_1 = spread_darkness(walled_tile_map_1, [true_history[i - 1][0] - 1, true_history[i - 1][1]])
        walled_tile_map_1 = spread_darkness(walled_tile_map_1, [true_history[i][0] - 1, true_history[i][1]])
    elif move == (1, 0):
        walled_tile_map_1 = spread_darkness(walled_tile_map_1, [true_history[i - 1][0], true_history[i - 1][1] + 1])
        walled_tile_map_1 = spread_darkness(walled_tile_map_1, [true_history[i][0], true_history[i][1] + 1])
    
    if move == (0, -1):
        walled_tile_map_2 = spread_darkness(walled_tile_map_2, [true_history[i - 1][0] - 1, true_history[i - 1][1]])
        walled_tile_map_2 = spread_darkness(walled_tile_map_2, [true_history[i][0] - 1, true_history[i][1]])
    elif move == (-1, 0):
        walled_tile_map_2 = spread_darkness(walled_tile_map_2, [true_history[i - 1][0], true_history[i - 1][1] + 1])
        walled_tile_map_2 = spread_darkness(walled_tile_map_2, [true_history[i][0], true_history[i][1] + 1])
    elif move == (0, 1):
        walled_tile_map_2 = spread_darkness(walled_tile_map_2, [true_history[i - 1][0] + 1, true_history[i - 1][1]])
        walled_tile_map_2 = spread_darkness(walled_tile_map_2, [true_history[i][0] + 1, true_history[i][1]])
    elif move == (1, 0):
        walled_tile_map_2 = spread_darkness(walled_tile_map_2, [true_history[i - 1][0], true_history[i - 1][1] - 1])
        walled_tile_map_2 = spread_darkness(walled_tile_map_2, [true_history[i][0], true_history[i][1] - 1])

# Walled tile map is correct by visual inspection
"""
for row in walled_tile_map_2:
    print("".join(row))
"""

s = 0
for row in walled_tile_map_2:
    for character in row:
        if character == ".":
            s += 1

print(s)

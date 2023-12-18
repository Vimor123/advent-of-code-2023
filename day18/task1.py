import sys

sys.setrecursionlimit(100000)


instructions = []

input_file = open("input.txt", "r")

for line in input_file:
    segments = line.strip().split()
    instructions.append({ "direction" : segments[0],
                          "steps" : int(segments[1]),
                          "color" : segments[2][1:-1] })

input_file.close()


history = []
position = (0, 0)

increments = {
    "L" : (0, -1),
    "U" : (-1, 0),
    "R" : (0, 1),
    "D" : (1, 0)
}

history.append((0, 0))

for instruction in instructions:
    increment = increments[instruction["direction"]]
    for step in range(instruction["steps"]):
        position = (position[0] + increment[0], position[1] + increment[1])
        history.append(position)


min_row = history[0][0]
min_column = history[0][1]

max_row = history[0][0]
max_column = history[0][1]

for position in history:
    if position[0] < min_row:
        min_row = position[0]
    if position[1] < min_column:
        min_column = position[1]
    if position[0] > max_row:
        max_row = position[0]
    if position[1] > max_column:
        max_column = position[1]


dig_map = []
for i in range(max_row - min_row + 1):
    dig_map.append(["-"] * (max_column - min_column + 1))

for position in history:
    dig_map[position[0] - min_row][position[1] - min_column] = "#"


def cut_space(dig_map, position):
    if position[0] < 0 or position[0] >= len(dig_map) or position[1] < 0 or position[1] >= len(dig_map[0]):
        return dig_map
    if dig_map[position[0]][position[1]] == "-":
        dig_map[position[0]][position[1]] = "."
        for move in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            dig_map = cut_space(dig_map, (position[0] + move[0], position[1] + move[1]))

    return dig_map


for i in range(0, len(dig_map)):
    dig_map = cut_space(dig_map, (i, 0))
    dig_map = cut_space(dig_map, (i, len(dig_map[0]) - 1))

for i in range(0, len(dig_map[0])):
    dig_map = cut_space(dig_map, (0, i))
    dig_map = cut_space(dig_map, (len(dig_map) - 1, i))


s = 0

for row in dig_map:
    for tile in row:
        if tile != ".":
            s += 1

print(s)

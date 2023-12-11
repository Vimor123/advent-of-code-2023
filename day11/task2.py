space_map = []

input_file = open("input.txt", "r")

for line in input_file:
    space_map.append(list(line.strip()))

input_file.close()

expanded_space_map = []

for i in range(len(space_map)):
    if "#" not in space_map[i]:
        expanded_space_map.append(["-"] * len(space_map[0]))
    else:
        expanded_space_map.append(space_map[i].copy())

for column_index in range(len(space_map[0])):
    column_empty = True
    for row_index in range(len(space_map)):
        if space_map[row_index][column_index] == "#":
            column_empty = False

    if column_empty:
        for row_index in range(len(expanded_space_map)):
            expanded_space_map[row_index][column_index] = "-"


galaxies_coords = []

for i in range(len(expanded_space_map)):
    for j in range(len(expanded_space_map[0])):
        if expanded_space_map[i][j] == "#":
            galaxies_coords.append((i, j))

def distance(space_map, coords1, coords2):
    space_multiplier = 1000000
    position = [coords1[0], coords1[1]]
    difference = [coords2[0] - coords1[0], coords2[1] - coords1[1]]

    distance = 0

    while difference[0] != 0:
        if difference[0] < 0:
            position[0] -= 1
            difference[0] += 1
        else:
            position[0] += 1
            difference[0] -= 1

        if space_map[position[0]][position[1]] == '-':
            distance += space_multiplier
        else:
            distance += 1

    while difference[1] != 0:
        if difference[1] < 0:
            position[1] -= 1
            difference[1] += 1
        else:
            position[1] += 1
            difference[1] -= 1

        if space_map[position[0]][position[1]] == '-':
            distance += space_multiplier
        else:
            distance += 1

    return distance

s = 0
for i in range(len(galaxies_coords)):
    for j in range(i, len(galaxies_coords)):
        s += distance(expanded_space_map, galaxies_coords[i], galaxies_coords[j])

print(s)

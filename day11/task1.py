space_map = []

input_file = open("input.txt", "r")

for line in input_file:
    space_map.append(list(line.strip()))

input_file.close()

expanded_space_map = []

for i in range(len(space_map)):
    expanded_space_map.append(space_map[i].copy())
    if "#" not in space_map[i]:
        expanded_space_map.append(space_map[i].copy())

esm_column_index = 0
for column_index in range(len(space_map[0])):
    column_empty = True
    for row_index in range(len(space_map)):
        if space_map[row_index][column_index] == "#":
            column_empty = False

    if column_empty:
        for row_index in range(len(expanded_space_map)):
            expanded_space_map[row_index].insert(esm_column_index, ".")
        esm_column_index += 1

    esm_column_index += 1

"""
for row in expanded_space_map:
    print("".join(row))
"""

galaxies_coords = []

for i in range(len(expanded_space_map)):
    for j in range(len(expanded_space_map[0])):
        if expanded_space_map[i][j] == "#":
            galaxies_coords.append((i, j))

def distance(coords1, coords2):
    return abs(coords2[0] - coords1[0]) + abs(coords2[1] - coords1[1])

s = 0
for i in range(len(galaxies_coords)):
    for j in range(i, len(galaxies_coords)):
        s += distance(galaxies_coords[i], galaxies_coords[j])

print(s)

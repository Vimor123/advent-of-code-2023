garden_map = []
starting_position = (-1, -1)

input_file = open("input.txt", "r")

for line_index, line in enumerate(input_file):
    garden_map.append(line.strip())
    if "S" in line:
        starting_position = (line_index, line.index("S"))

input_file.close()


def get_neighbours(garden_map, current_position):
    neighbours = []
    for increment in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
        new_position = (current_position[0] + increment[0], current_position[1] + increment[1])
        if new_position[0] < 0 or new_position[0] >= len(garden_map) or new_position[1] < 0 or new_position[1] >= len(garden_map[0]):
            continue
        if garden_map[new_position[0]][new_position[1]] == "#":
            continue

        neighbours.append(new_position)
    return neighbours


positions = [starting_position]

for i in range(64):
    new_positions = []
    for position in positions:
        new_positions_1 = get_neighbours(garden_map, position)
        for new_position in new_positions_1:
            if new_position not in new_positions:
                new_positions.append(new_position)

    positions = new_positions

print(len(new_positions))

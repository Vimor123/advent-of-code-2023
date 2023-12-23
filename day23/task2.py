import sys

sys.setrecursionlimit(1000000)

hiking_map = []

input_file = open("input.txt", "r")

for line in input_file:
    hiking_map.append(list(line.strip()))

input_file.close()

starting_position = (-1, -1)
for tile_index, tile in enumerate(hiking_map[0]):
    if tile == ".":
        starting_position = (0, tile_index)


def get_longest_path(hiking_map, position, visited_positions):
    new_visited_positions = visited_positions.copy()
    new_visited_positions.append(position)

    if position[0] == len(hiking_map) - 1:
        return len(new_visited_positions) - 1

    longest_new_path = 0
    move_possible = False

    for increment in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
        new_position = (position[0] + increment[0], position[1] + increment[1])
        if new_position[0] < 0 or new_position[0] >= len(hiking_map) or new_position[1] < 0 or new_position[1] >= len(hiking_map[0]):
            continue
        if hiking_map[new_position[0]][new_position[1]] == "#":
            continue
        if new_position in new_visited_positions:
            continue

        move_possible = True
        new_path_length = get_longest_path(hiking_map, new_position, new_visited_positions.copy())
        if new_path_length > longest_new_path:
            longest_new_path = new_path_length

    if not move_possible:
        return -100000
    else:
        return longest_new_path


print(get_longest_path(hiking_map, starting_position, []))

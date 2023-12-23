# Credit: HyperNeutrino

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


def fill(starting_position, steps):
    reached_positions = []
    visited = [starting_position]
    positions_to_visit = [{"position" : starting_position, "remaining_steps" : steps}]

    while len(positions_to_visit) > 0:
        position_to_visit = positions_to_visit.pop(0)
        if position_to_visit["remaining_steps"] % 2 == 0:
            reached_positions.append(position_to_visit["position"])
        if position_to_visit["remaining_steps"] == 0:
            continue

        neighbours = get_neighbours(garden_map, position_to_visit["position"])

        for neighbour in neighbours:
            if neighbour in visited:
                continue
            visited.append(neighbour)
            positions_to_visit.append({"position" : neighbour, "remaining_steps" : position_to_visit["remaining_steps"] - 1})

    return len(reached_positions)


steps = 26501365
garden_map_size = len(garden_map)

assert garden_map_size == len(garden_map[0])
assert steps % garden_map_size == starting_position[0] == starting_position[1]

grid_width = steps // garden_map_size - 1

odd_grids = (grid_width // 2 * 2 + 1) ** 2
even_grids = ((grid_width + 1) // 2 * 2) ** 2

odd_points = fill(starting_position, garden_map_size * 2 + 1)
even_points = fill(starting_position, garden_map_size * 2)

print("Odds and evens calculated.")

total = odd_grids * odd_points + even_grids * even_points


corner_top = fill((garden_map_size - 1, starting_position[1]), garden_map_size - 1)
corner_right = fill((starting_position[0], 0), garden_map_size - 1)
corner_bottom = fill((0, starting_position[1]), garden_map_size - 1)
corner_left = fill((starting_position[0], garden_map_size - 1), garden_map_size - 1)

print("Corners calculated.")

total += corner_top + corner_right + corner_bottom + corner_left


small_edge_top_right = fill((garden_map_size - 1, 0), garden_map_size // 2 - 1)
small_edge_bottom_right = fill((0, 0), garden_map_size // 2 - 1)
small_edge_bottom_left = fill((0, garden_map_size - 1), garden_map_size // 2 - 1)
small_edge_top_left = fill((garden_map_size - 1, garden_map_size - 1), garden_map_size // 2 - 1)

print("Small edges calculated.")

total += (grid_width + 1) * (small_edge_top_right + small_edge_bottom_right + small_edge_bottom_left + small_edge_top_left)


big_edge_top_right = fill((garden_map_size - 1, 0), 3 * garden_map_size // 2 - 1)
big_edge_bottom_right = fill((0, 0), 3 * garden_map_size // 2 - 1)
big_edge_bottom_left = fill((0, garden_map_size - 1), 3 * garden_map_size // 2 - 1)
big_edge_top_left = fill((garden_map_size - 1, garden_map_size - 1), 3 * garden_map_size // 2 - 1)

print("Big edges calculated.")

total += grid_width * (big_edge_top_right + big_edge_bottom_right + big_edge_bottom_left + big_edge_top_left)


print("Total:", total)

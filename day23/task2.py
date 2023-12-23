hiking_map = []

input_file = open("input.txt", "r")

for line in input_file:
    hiking_map.append(list(line.strip()))

input_file.close()

starting_position = (-1, -1)
for tile_index, tile in enumerate(hiking_map[0]):
    if tile == ".":
        starting_position = (0, tile_index)


def get_neighbours(hiking_map, position):
    neighbours = []
    for increment in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
        new_position = (position[0] + increment[0], position[1] + increment[1])
        if new_position[0] < 0 or new_position[0] >= len(hiking_map) or new_position[1] < 0 or new_position[1] >= len(hiking_map[1]):
            continue
        if hiking_map[new_position[0]][new_position[1]] == "#":
            continue
        neighbours.append(new_position)
    return neighbours


print("Calculating graph positions.")

graph_positions = [starting_position]

visited_positions = []
positions_to_visit = [starting_position]

while len(positions_to_visit) > 0:
    position = positions_to_visit.pop(0)
    visited_positions.append(position)

    neighbours = get_neighbours(hiking_map, position)
    unvisited_neighbours = []
    for neighbour in neighbours:
        if neighbour not in visited_positions:
            unvisited_neighbours.append(neighbour)

    while len(unvisited_neighbours) == 1:
        position = unvisited_neighbours[0]
        visited_positions.append(position)

        neighbours = get_neighbours(hiking_map, position)
        unvisited_neighbours = []
        for neighbour in neighbours:
            if neighbour not in visited_positions:
                unvisited_neighbours.append(neighbour)

    if len(unvisited_neighbours) > 0:
        graph_positions.append(position)
        for unvisited_neighbour in unvisited_neighbours:
            positions_to_visit.append(unvisited_neighbour)

    if position[0] == len(hiking_map) - 1:
        graph_positions.append(position)


def calculate_neighbour_distances(hiking_map, position):
    neighbour_distances = []
    neighbours = get_neighbours(hiking_map, position)
    
    for neighbour in neighbours:
        visited = [position, neighbour]

        new_neighbours = get_neighbours(hiking_map, neighbour)
        unvisited_neighbours = []
        for new_neighbour in new_neighbours:
            if new_neighbour not in visited:
                unvisited_neighbours.append(new_neighbour)

        path_length = 1
        while len(unvisited_neighbours) == 1:
            path_length += 1
            new_position = unvisited_neighbours[0]
            visited.append(new_position)

            new_neighbours = get_neighbours(hiking_map, new_position)
            unvisited_neighbours = []
            for new_neighbour in new_neighbours:
                if new_neighbour not in visited:
                    unvisited_neighbours.append(new_neighbour)

        if new_position in graph_positions:
            neighbour_distances.append({"neighbour" : new_position, "distance" : path_length})

    return neighbour_distances


hiking_graph = {}

print("Calculating neighbour distances for graph position.")

for graph_position in graph_positions:
    hiking_graph[graph_position] = calculate_neighbour_distances(hiking_map, graph_position)


def get_longest_path(hiking_graph, position, visited_positions):
    new_visited_positions = visited_positions.copy()
    new_visited_positions.append(position)

    if position[0] == len(hiking_map) - 1:
        return 0

    longest_path = 0
    move_possible = False

    for neighbour_distance in hiking_graph[position]:
        if neighbour_distance["neighbour"] in new_visited_positions:
            continue

        path_length = neighbour_distance["distance"] + get_longest_path(hiking_graph, neighbour_distance["neighbour"], new_visited_positions.copy())

        move_possible = True

        if path_length > longest_path:
            longest_path = path_length

    if not move_possible:
        return -100000

    else:
        return longest_path

print("Seeking longest path.")
print("Longest path:", get_longest_path(hiking_graph, starting_position, []))

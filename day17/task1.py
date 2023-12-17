import sys

sys.setrecursionlimit(100000000)

heat_loss_map = []

distance_maps = {}

for move in ["left", "up", "down", "right"]:
    for remaining_straights in range(4):
        distance_maps[(move, remaining_straights)] = []

input_file = open("input1.txt", "r")

for line in input_file:
    heat_loss_map.append([int(x) for x in list(line.strip())])
    for move in ["left", "up", "down", "right"]:
        for remaining_straights in range(4):
            distance_maps[(move, remaining_straights)].append([-1] * len(line.strip()))

input_file.close()


def generate_neighbours(node):
    increment_directions = {
        (0, -1) : "left",
        (-1, 0) : "up",
        (0, 1) : "righ",
        (1, 0) : "down"
    }
    all_increments = {
        "left" : [(1, 0), (0, -1), (-1, 0)],
        "up" : [(0, -1), (-1, 0), (0, 1)],
        "right" : [(-1, 0), (0, 1), (1, 0)],
        "down" : [(0, 1), (1, 0), (0, -1)]
    }

    new_nodes = []

    for increment in all_increments[node["direction"]]:
        new_position = (node["position"][0] + increment[0], node["position"][1] + increment[1])
        if new_position[0] < 0 or new_position[0] >= len(heat_loss_map) or new_position[1] < 0 or new_position[1] >= len(heat_loss_map[0]):
            continue

        new_direction = direction_increments[increment]
        new_straights = 3
        if new_direction == node["direction"]:
            new_straights = node["straights_remaining"] - 1

        new_nodes.append({ "position" : new_position, "direction" : new_direction, "straights_remaining" : new_straights })

    return new_nodes


start_1 = { "position" : (0, 0), "direction" : "right", "straights_remaining" : 3 }
start_2 = { "position" : (0, 0), "direction" : "down", "straights_remaining" : 3 }
distance = 0

work = ""

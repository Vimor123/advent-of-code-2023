import sys

sys.setrecursionlimit(100000000)

heat_loss_map = []

input_file = open("input.txt", "r")

for line in input_file:
    heat_loss_map.append([int(x) for x in list(line.strip())])

input_file.close()


turning = {
        "left" : { "turn_left" : "down", "turn_right" : "up" },
        "up" : { "turn_left" : "left", "turn_right" : "right" },
        "right" : { "turn_left" : "up", "turn_right" : "down" },
        "down" : { "turn_left" : "left", "turn_right" : "right" }
}

increments = {
        "left" : (0, -1),
        "up" : (-1, 0),
        "right" : (0, 1),
        "down" : (1, 0)
}


nodes_to_visit = [{ "distance" : 0, "position" : (0, 0), "direction" : "right", "remaining_straights" : 3 },
                  { "distance" : 0, "position" : (0, 0), "direction" : "down", "remaining_straights" : 3 }]


def position_on_map(position):
    if position[0] < 0 or position[0] >= len(heat_loss_map) or position[1] < 0 or position[1] >= len(heat_loss_map):
        return False
    return True

iteration = 0

visited = {}

while len(nodes_to_visit) > 0:
    min_distance_node_index = -1
    min_distance = -1
    for node_index, node in enumerate(nodes_to_visit):
        if node["distance"] < min_distance or min_distance < 0:
            min_distance = node["distance"]
            min_distance_node_index = node_index

    node = nodes_to_visit.pop(min_distance_node_index)

    node_without_distance = (node["position"], node["direction"], node["remaining_straights"] )

    if node_without_distance in visited:
        continue

    visited[node_without_distance] = node["distance"]

    # Turn left
    new_direction_1 = turning[node["direction"]]["turn_left"]
    increment = increments[new_direction_1]
    new_position_1 = (node["position"][0] + increment[0], node["position"][1] + increment[1])

    if position_on_map(new_position_1):
        new_node = {
            "distance" : node["distance"] + heat_loss_map[new_position_1[0]][new_position_1[1]],
            "position" : new_position_1,
            "direction" : new_direction_1,
            "remaining_straights" : 2
        }
        nodes_to_visit.append(new_node)

    # Turn right
    new_direction_2 = turning[node["direction"]]["turn_right"]
    increment = increments[new_direction_2]
    new_position_2 = (node["position"][0] + increment[0], node["position"][1] + increment[1])

    if position_on_map(new_position_2):
        new_node = {
            "distance" : node["distance"] + heat_loss_map[new_position_2[0]][new_position_2[1]],
            "position" : new_position_2,
            "direction" : new_direction_2,
            "remaining_straights" : 2
        }
        nodes_to_visit.append(new_node)

    # Continue straight
    increment = increments[node["direction"]]
    new_position_3 = (node["position"][0] + increment[0], node["position"][1] + increment[1])

    if position_on_map(new_position_3) and node["remaining_straights"] > 0:
        new_node = {
            "distance" : node["distance"] + heat_loss_map[new_position_3[0]][new_position_3[1]],
            "position" : new_position_3,
            "direction" : node["direction"],
            "remaining_straights" : node["remaining_straights"] - 1
        }
        nodes_to_visit.append(new_node)

    iteration += 1

    if iteration % 10000 == 0:
        print(iteration, len(nodes_to_visit))


min_distance = -1
for node, distance in visited.items():
    if node[0][0] == len(heat_loss_map) - 1 and node[0][1] == len(heat_loss_map[0]) - 1:
        if min_distance > distance or min_distance < 0:
            min_distance = distance

print(min_distance)

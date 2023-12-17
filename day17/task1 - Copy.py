import sys

sys.setrecursionlimit(100000000)

heat_loss_map = []

distances_map = []

input_file = open("input1.txt", "r")

for line in input_file:
    heat_loss_map.append([int(x) for x in list(line.strip())])

    distances_map.append([])
    for i in range(len(line.strip())):
        distances = {}
        for straights_remaining in range(3):
            for direction in ["left", "up", "right", "down"]:
                distances[(straights_remaining, direction)] = -1
        distances_map[-1].append(distances)

input_file.close()

for straights_remaining in range(3):
            for direction in ["left", "up", "right", "down"]:
                distances_map[0][0][(straights_remaining, direction)] = 0

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


def position_on_map(position):
    if position[0] < 0 or position[0] >= len(heat_loss_map) or position[1] < 0 or position[1] >= len(heat_loss_map):
        return False
    return True


def search_path(current_loss, position, direction, straights_remaining):
    left_valid = False
    right_valid = False
    straight_valid = False

    # Turn left
    new_direction_1 = turning[direction]["turn_left"]
    increment = increments[new_direction_1]
    new_position_1 = (position[0] + increment[0], position[1] + increment[1])
    if position_on_map(new_position_1):
        new_loss = current_loss + heat_loss_map[new_position_1[0]][new_position_1[1]]
        if new_loss < distances_map[new_position_1[0]][new_position_1[1]][(2, new_direction_1)] or distances_map[new_position_1[0]][new_position_1[1]][(2, new_direction_1)] < 0:
            for i in range(3):
                distances_map[new_position_1[0]][new_position_1[1]][(i, new_direction_1)] = new_loss
            search_path(new_loss, new_position_1, new_direction_1, 2)
            

    # Turn right
    new_direction_2 = turning[direction]["turn_right"]
    increment = increments[new_direction_2]
    new_position_2 = (position[0] + increment[0], position[1] + increment[1])
    if position_on_map(new_position_2):
        new_loss = current_loss + heat_loss_map[new_position_2[0]][new_position_2[1]]
        if new_loss < distances_map[new_position_2[0]][new_position_2[1]][(2, new_direction_2)] or distances_map[new_position_2[0]][new_position_2[1]][(2, new_direction_2)] < 0:
            for i in range(3):
                distances_map[new_position_2[0]][new_position_2[1]][(i, new_direction_2)] = new_loss
            search_path(new_loss, new_position_2, new_direction_2, 2)

    # Continue straight
    increment = increments[direction]
    new_position_3 = (position[0] + increment[0], position[1] + increment[1])
    if position_on_map(new_position_3) and straights_remaining > 0:
        new_loss = current_loss + heat_loss_map[new_position_3[0]][new_position_3[1]]
        new_straights_remaining = straights_remaining - 1
        if new_loss < distances_map[new_position_3[0]][new_position_3[1]][(new_straights_remaining, direction)] or distances_map[new_position_3[0]][new_position_3[1]][(new_straights_remaining, direction)] < 0:
            for i in range(new_straights_remaining + 1):
                distances_map[new_position_3[0]][new_position_3[1]][(i, direction)] = new_loss
            search_path(new_loss, new_position_3, direction, new_straights_remaining)





loss = 0
search_path(loss, (0, 0), "right", 3)
search_path(loss, (0, 0), "down", 3)

min_distance = -1

for distance in distances_map[-1][-1].values():
    if distance > 0:
        if min_distance < 0 or min_distance > distance:
            min_distance = distance

print(min_distance)

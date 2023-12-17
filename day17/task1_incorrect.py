import sys

sys.setrecursionlimit(100000000)

heat_loss_map = []

distance_map = []

input_file = open("input1.txt", "r")

for line in input_file:
    heat_loss_map.append([int(x) for x in list(line.strip())])
    distance_map.append([-1] * len(line.strip()))

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


def position_on_map(position):
    if position[0] < 0 or position[0] >= len(heat_loss_map) or position[1] < 0 or position[1] >= len(heat_loss_map):
        return False
    return True

max_manhattan = 0
true_max = len(heat_loss_map) + len(heat_loss_map[0]) - 2

def search_path(current_loss, position, direction, straight_moves_remaining):
    global max_manhattan

    if current_loss > distance_map[position[0]][position[1]] and distance_map[position[0]][position[1]] >= 0:
        return

    manhattan_distance = position[0] + position[1]
    if manhattan_distance > max_manhattan:
        max_manhattan = manhattan_distance
        print("{}/{}".format(max_manhattan, true_max))

    distance_map[position[0]][position[1]] = current_loss

    left_valid = False
    right_valid = False
    straight_valid = False

    # Turn left
    new_direction_1 = turning[direction]["turn_left"]
    increment = increments[new_direction_1]
    new_position_1 = (position[0] + increment[0], position[1] + increment[1])
    if position_on_map(new_position_1):
        new_loss = current_loss + heat_loss_map[new_position_1[0]][new_position_1[1]]
        if new_loss < distance_map[new_position_1[0]][new_position_1[1]] or distance_map[new_position_1[0]][new_position_1[1]] < 0:
            search_path(new_loss, new_position_1, new_direction_1, 3)

    # Turn right
    new_direction_2 = turning[direction]["turn_right"]
    increment = increments[new_direction_2]
    new_position_2 = (position[0] + increment[0], position[1] + increment[1])
    if position_on_map(new_position_2):
        new_loss = current_loss + heat_loss_map[new_position_2[0]][new_position_2[1]]
        if new_loss < distance_map[new_position_2[0]][new_position_2[1]] or distance_map[new_position_2[0]][new_position_2[1]] < 0:
            search_path(new_loss, new_position_2, new_direction_2, 3)

    # Continue straight
    increment = increments[direction]
    new_position_3 = (position[0] + increment[0], position[1] + increment[1])
    if position_on_map(new_position_3) and straight_moves_remaining > 0:
        new_loss = current_loss + heat_loss_map[new_position_3[0]][new_position_3[1]]
        if new_loss < distance_map[new_position_3[0]][new_position_3[1]] or distance_map[new_position_3[0]][new_position_3[1]] < 0:
            search_path(new_loss, new_position_3, direction, straight_moves_remaining - 1)

loss = 0
search_path(loss, (0, 0), "right", 3)
search_path(loss, (0, 0), "down", 3)

print(distance_map[-1][-1])

for row in distance_map:
    print(row)

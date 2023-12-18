# Credit : HyperNeutrino

import sys

sys.setrecursionlimit(100000)


instructions = []

input_file = open("input.txt", "r")

for line in input_file:
    segments = line.strip().split()
    
    true_instruction_string = segments[2][2:-1]

    true_direction = "N"
    if true_instruction_string.endswith("0"):
        true_direction = "R"
    elif true_instruction_string.endswith("1"):
        true_direction = "D"
    elif true_instruction_string.endswith("2"):
        true_direction = "L"
    elif true_instruction_string.endswith("3"):
        true_direction = "U"

    true_steps_string = true_instruction_string[:-1]
    true_steps = int(true_steps_string, 16)

    instructions.append({ "direction" : true_direction,
                          "steps" : true_steps,
                          "color" : "Bloody none" })


input_file.close()


history = []
position = (0, 0)

increments = {
    "L" : (0, -1),
    "U" : (-1, 0),
    "R" : (0, 1),
    "D" : (1, 0)
}

history.append((0, 0))

boundaries = 0

for instruction in instructions:
    increment = increments[instruction["direction"]]
    position = (position[0] + increment[0] * instruction["steps"], position[1] + increment[1] * instruction["steps"])
    boundaries += instruction["steps"]
    history.append(position)

history.pop(len(history) - 1)


# Shoelace

area = history[0][0] * (history[len(history) - 1][1] - history[1][1])
for i in range(1, len(history) - 1):
    area += history[i][0] * (history[i - 1][1] - history[i + 1][1])
area += history[len(history) - 1][0] * (history[len(history) - 2][1] - history[0][1])

area = abs(area) // 2


# Pick

internal_tiles = area - (boundaries // 2) + 1


print(internal_tiles + boundaries)

rock_map = []

input_file = open("input.txt", "r")

for line in input_file:
    rock_map.append(list(line.strip()))

input_file.close()

def tilt_north(rock_map):
    for column_index in range(len(rock_map[0])):
        for row_index in range(len(rock_map)):
            space = rock_map[row_index][column_index]
            if space == "O":
                current_row = row_index
                while current_row > 0:
                    if rock_map[current_row - 1][column_index] == ".":
                        rock_map[current_row][column_index] = "."
                        rock_map[current_row - 1][column_index] = "O"
                        current_row -= 1
                    else:
                        break
    return rock_map

def tilt_south(rock_map):
    for column_index in range(len(rock_map[0])):
        for row_index in range(len(rock_map) - 1, -1, -1):
            space = rock_map[row_index][column_index]
            if space == "O":
                current_row = row_index
                while current_row < len(rock_map) - 1:
                    if rock_map[current_row + 1][column_index] == ".":
                        rock_map[current_row][column_index] = "."
                        rock_map[current_row + 1][column_index] = "O"
                        current_row += 1
                    else:
                        break
    return rock_map

def tilt_west(rock_map):
    for row_index in range(len(rock_map)):
        for column_index in range(len(rock_map[0])):
            space = rock_map[row_index][column_index]
            if space == "O":
                current_column = column_index
                while current_column > 0:
                    if rock_map[row_index][current_column - 1] == ".":
                        rock_map[row_index][current_column] = "."
                        rock_map[row_index][current_column - 1] = "O"
                        current_column -= 1
                    else:
                        break
    return rock_map

def tilt_east(rock_map):
    for row_index in range(len(rock_map)):
        for column_index in range(len(rock_map[0]) - 1, -1 , -1):
            space = rock_map[row_index][column_index]
            if space == "O":
                current_column = column_index
                while current_column < len(rock_map[0]) - 1:
                    if rock_map[row_index][current_column + 1] == ".":
                        rock_map[row_index][current_column] = "."
                        rock_map[row_index][current_column + 1] = "O"
                        current_column += 1
                    else:
                        break
    return rock_map


previous_rock_maps = []

i = 0

cycle_detected = False

while i < 1000000000:
    previous_rock_map = []
    for row in rock_map:
        previous_rock_map.append(row.copy())

    previous_rock_maps.append(previous_rock_map)
    
    rock_map = tilt_north(rock_map)
    rock_map = tilt_west(rock_map)
    rock_map = tilt_south(rock_map)
    rock_map = tilt_east(rock_map)

    if not cycle_detected:
        cycle_length = 0

        for pi, previous_rock_map in enumerate(previous_rock_maps):
            same_as_previous = True
            for previous_row, row in zip(previous_rock_map, rock_map):
                if previous_row != row:
                    same_as_previous = False

            if same_as_previous:
                cycle_detected = True
                cycle_length = i - pi + 1
                break

        if cycle_detected:
            li = i
            rem = 1000000000 - li - 1
            to_do = rem % cycle_length
            i = 1000000000 - to_do - 1

    i += 1


s = 0

for row_index, row in enumerate(rock_map):
    for element in row:
        if element == "O":
            s += len(rock_map) - row_index

print(s)

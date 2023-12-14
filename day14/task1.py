rock_map = []

input_file = open("input.txt", "r")

for line in input_file:
    rock_map.append(list(line.strip()))

input_file.close()

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


s = 0

for row_index, row in enumerate(rock_map):
    for element in row:
        if element == "O":
            s += len(rock_map) - row_index

print(s)

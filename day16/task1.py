grid = {}

visited = []

input_file = open("input.txt", "r")

for li, line in enumerate(input_file):
    visited.append([])
    for ci, character in enumerate(list(line.strip())):
        if character in ["|", "-", "/", "\\"]:
            grid[(li, ci)] = character
        visited[-1].append(".")

input_file.close()

right_bound = len(visited[0])
lower_bound = len(visited)


journey = []

def send_ray(position, direction):
    direction_map = { "left" : (0, -1),
                      "up" : (-1, 0),
                      "right" : (0, 1),
                      "down" : (1, 0) }

    position_on_map = True
    if not (position[0] >= 0 and position[0] < lower_bound and position[1] >= 0 and position[1] < right_bound):
        position_on_map = False

    while position_on_map:
        visited[position[0]][position[1]] = "#"

        if (position, direction) in journey:
            return
        journey.append((position, direction))

        new_position = (position[0] + direction_map[direction][0], position[1] + direction_map[direction][1])

        if not (new_position[0] >= 0 and new_position[0] < lower_bound and new_position[1] >= 0 and new_position[1] < right_bound):
            position_on_map = False
            break

        position = new_position

        if position in grid:
            if grid[position] == "/":
                if direction == "left":
                    direction = "down"
                elif direction == "up":
                    direction = "right"
                elif direction == "right":
                    direction = "up"
                else:
                    direction = "left"

            elif grid[position] == "\\":
                if direction == "left":
                    direction = "up"
                elif direction == "up":
                    direction = "left"
                elif direction == "right":
                    direction = "down"
                else:
                    direction = "right"

            elif grid[position] == "|":
                if direction == "left" or direction == "right":
                    direction = "up"
                    send_ray(position, "down")

            else:
                if direction == "up" or direction == "down":
                    direction = "left"
                    send_ray(position, "right")


send_ray((0, 0), "down")

s = 0

for row in visited:
    for character in row:
        if character == "#":
            s += 1

print(s)

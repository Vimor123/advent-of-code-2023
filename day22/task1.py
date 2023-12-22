bricks = []

input_file = open("input.txt", "r")

for line in input_file:
    brick_strings = line.strip().split("~")
    bricks.append(([int(x) for x in brick_strings[0].split(",")],
                   [int(x) for x in brick_strings[1].split(",")]))

input_file.close()


sorted_bricks = sorted(bricks, key = lambda brick: min(brick[0][2], brick[1][2]))

max_x = 0
max_y = 0

for brick in sorted_bricks:
    if max(brick[0][0], brick[1][0]) > max_x:
        max_x = max(brick[0][0], brick[1][0])
    if max(brick[0][1], brick[1][1]) > max_y:
        max_y = max(brick[0][1], brick[1][1])

height_map = []
for i in range(max_x + 1):
    height_map.append([])
    for i in range(max_y + 1):
        height_map[-1].append({"height" : 0, "last_brick" : -1})

supports = []

for i in range(len(sorted_bricks)):
    brick = sorted_bricks[i]
    current_height = min(brick[0][2], brick[1][2])

    x_covers = (min(brick[0][0], brick[1][0]), max(brick[0][0], brick[1][0]))
    y_covers = (min(brick[0][1], brick[1][1]), max(brick[0][1], brick[1][1]))

    maximal_height_on_cover = -1
    supports_for_brick = []
    for x in range(x_covers[0], x_covers[1] + 1):
        for y in range(y_covers[0], y_covers[1] + 1):
            if height_map[x][y]["height"] > maximal_height_on_cover:
                maximal_height_on_cover = height_map[x][y]["height"]
                supports_for_brick = [height_map[x][y]["last_brick"]]
            elif height_map[x][y]["height"] == maximal_height_on_cover:
                if height_map[x][y]["last_brick"] not in supports_for_brick:
                    supports_for_brick.append(height_map[x][y]["last_brick"])

    supports.append(supports_for_brick)

    if current_height < maximal_height_on_cover + 1:
        print("Error, brick too low")

    brick_z_0 = brick[0][2]
    brick_z_1 = brick[1][2]

    if brick_z_0 < brick_z_1:
        diff = brick_z_1 - brick_z_0
        brick_z_0 = maximal_height_on_cover + 1
        brick_z_1 = brick_z_0 + diff
    else:
        diff = brick_z_0 - brick_z_1
        brick_z_1 = maximal_height_on_cover + 1
        brick_z_0 = brick_z_1 + diff

    sorted_bricks[i][0][2] = brick_z_0
    sorted_bricks[i][1][2] = brick_z_1

    for x in range(x_covers[0], x_covers[1] + 1):
        for y in range(y_covers[0], y_covers[1] + 1):
            height_map[x][y]["height"] = max(sorted_bricks[i][0][2], sorted_bricks[i][1][2])
            height_map[x][y]["last_brick"] = i


safe_disintegrations = 0

for i in range(len(sorted_bricks)):
    can_be_disintegrated = True
    for j in range(i + 1, len(sorted_bricks)):
        if i in supports[j] and len(supports[j]) == 1:
            can_be_disintegrated = False
            break

    if can_be_disintegrated:
        safe_disintegrations += 1

print(safe_disintegrations)

hailstones = []

input_file = open("input.txt", "r")

for line in input_file:
    position, velocity = line.strip().split(" @ ")
    position = tuple([int(x) for x in position.split(", ")])
    velocity = tuple([int(x) for x in velocity.split(", ")])
    hailstones.append({"position" : position, "velocity" : velocity})

input_file.close()


def intersection2D(hailstone1, hailstone2):
    # y1 = a1 * x + b1
    # y2 = a2 * x + b2

    point1_h1 = (hailstone1["position"][0], hailstone1["position"][1])
    point2_h1 = (hailstone1["position"][0] + hailstone1["velocity"][0],
                 hailstone1["position"][1] + hailstone1["velocity"][1])

    vertical_line_h1 = False

    if point1_h1[0] != point2_h1[0]:
        a_h1 = (point2_h1[1] - point1_h1[1]) / (point2_h1[0] - point1_h1[0])
        b_h1 = point1_h1[1] - a_h1 * point1_h1[0]
    else:
        vertical_line_h1 = True
        x_h1 = point1_h1[0]

    point1_h2 = (hailstone2["position"][0], hailstone2["position"][1])
    point2_h2 = (hailstone2["position"][0] + hailstone2["velocity"][0],
                 hailstone2["position"][1] + hailstone2["velocity"][1])

    vertical_line_h2 = False

    if point1_h2[0] != point2_h2[0]:
        a_h2 = (point2_h2[1] - point1_h2[1]) / (point2_h2[0] - point1_h2[0])
        b_h2 = point1_h2[1] - a_h2 * point1_h2[0]
    else:
        vertical_line_h2 = True
        x_h2 = point1_h2[0]

    # a1 * x + b1 = a2 * x + b2
    # a1 * x - a2 * x = b2 - b1
    # (a1 - a2) * x = b2 - b1
    # x = (b2 - b1)/(a1 - a2)

    if not vertical_line_h1 and not vertical_line_h2:
        if a_h1 == a_h2:
            if b_h1 == b_h2:
                return True, ("all", "all")
            else:
                return False, (0, 0)
        else:
            x = (b_h2 - b_h1) / (a_h1 - a_h2)
            y = a_h1 * x + b_h1
            return True, (x, y)

    elif vertical_line_h1 and vertical_line_h2:
        if x_h1 == x_h2:
            return True, ("all", "all")
        else:
            return False, (0, 0)

    elif vertical_line_h1:
        y = a_h2 * x_h1 + b_h2
        return True, (x_h1, y)

    else:
        y = a_h1 * x_h2 + b_h1
        return True, (x_h2, y)


def intersection_in_past_2D(hailstone1, hailstone2, intersection):
    if intersection == ("all", "all"):
        return False

    if hailstone1["velocity"][0] > 0:
        if intersection[0] < hailstone1["position"][0]:
            return True
    if hailstone1["velocity"][0] < 0:
        if intersection[0] > hailstone1["position"][0]:
            return True
    if hailstone1["velocity"][0] == 0:
        if hailstone1["velocity"][1] > 0:
            if intersection[1] < hailstone1["position"][1]:
                return True
        if hailstone1["velocity"][1] < 0:
            if intersection[1] > hailstone1["position"][1]:
                return True

    if hailstone2["velocity"][0] > 0:
        if intersection[0] < hailstone2["position"][0]:
            return True
    if hailstone2["velocity"][0] < 0:
        if intersection[0] > hailstone2["position"][0]:
            return True
    if hailstone2["velocity"][0] == 0:
        if hailstone2["velocity"][1] > 0:
            if intersection[1] < hailstone2["position"][1]:
                return True
        if hailstone2["velocity"][1] < 0:
            if intersection[1] > hailstone2["position"][1]:
                return True


s = 0

test_area = (200000000000000, 400000000000000)

for i in range(len(hailstones)):
    for j in range(i + 1, len(hailstones)):
        check, intersection = intersection2D(hailstones[i], hailstones[j])
        if not check:
            continue
        if intersection_in_past_2D(hailstones[i], hailstones[j], intersection):
            continue
        if intersection[0] < test_area[0] or intersection[0] > test_area[1]:
            continue
        if intersection[1] < test_area[0] or intersection[1] > test_area[1]:
            continue

        s += 1

print(s)

hailstones = []

input_file = open("input1.txt", "r")

for line in input_file:
    position, velocity = line.strip().split(" @ ")
    position = tuple([int(x) for x in position.split(", ")])
    velocity = tuple([int(x) for x in velocity.split(", ")])
    hailstones.append({"position" : position, "velocity" : velocity})

input_file.close()


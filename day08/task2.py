import math

input_file = open("input.txt", "r")

movements = input_file.readline().strip()

fake_tree = {}

for line in input_file:
    if line.strip() != "":
        node = line.split("=")[0].strip()
        children = line.split("=")[1].strip()
        children = children[1:-1].split(",")
        for i in range(len(children)):
            children[i] = children[i].strip()

        fake_tree[node] = children

input_file.close()

current_nodes = []
for node in list(fake_tree.keys()):
    if node.endswith("A"):
        current_nodes.append(node)

steps = []
for node in current_nodes:
    current_node = node
    destination_reached = False
    move = 0

    while not destination_reached:
        current_move = movements[move % len(movements)]
        if current_move == "L":
            current_node = fake_tree[current_node][0]
        else:
            current_node = fake_tree[current_node][1]

        move += 1

        if current_node.endswith("Z"):
            destination_reached = True

    cycle_achieved = False
    move_count = move
    desired_end = current_node

    while not cycle_achieved:
        current_move = movements[move_count % len(movements)]

        if current_move == "L":
            current_node = fake_tree[current_node][0]
        else:
            current_node = fake_tree[current_node][1]

        move_count += 1

        if current_node == desired_end:
            cycle_achieved = True

    steps.append((move, move_count - move))

reached = []
for step in steps:
    reached.append(step[0])

numbers = [step[1] for step in steps]

print(numbers)

print(math.lcm(15871, 16409, 21251, 18023, 12643, 19099))

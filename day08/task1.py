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

destination_reached = False
move = 0
current_node = "AAA"

while not destination_reached:
    current_move = movements[move % len(movements)]
    if current_move == "L":
        current_node = fake_tree[current_node][0]
    else:
        current_node = fake_tree[current_node][1]

    move += 1

    if current_node == "ZZZ":
        destination_reached = True

print(move)

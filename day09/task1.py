sequences = []

input_file = open("input.txt", "r")

for line in input_file:
    sequences.append([int(x) for x in line.strip().split()])

input_file.close()


s = 0

for sequence in sequences:
    current_sequence = sequence.copy()
    differences = []
    level = -1
    all_zeroes = False

    while not all_zeroes:
        level += 1
        differences.append([])
        all_zeroes = True
        for i in range(len(current_sequence) - 1):
            difference = current_sequence[i + 1] - current_sequence[i]
            if difference != 0:
                all_zeroes = False
            differences[level].append(difference)

        current_sequence = differences[level]

    next_value = 0
    level -= 1

    while level != -1:
        next_value = differences[level][-1] + next_value
        level -= 1

    next_value += sequence[-1]

    s += next_value

print(s)

spring_groups = []

input_file = open("input1.txt", "r")

for line in input_file:
    springs = list(line.split()[0])
    damaged_groups = [int(x) for x in line.strip().split()[1].split(",")]
    spring_groups.append({ "springs" : springs, "damaged" : damaged_groups })

input_file.close()


def get_binary_list(number, no_of_vars):
    binary_number = []
    while number > 0:
        if number % 2 == 1:
            binary_number.append(1)
        else:
            binary_number.append(0)
        number //= 2
    while len(binary_number) < no_of_vars:
        binary_number.append(0)
    binary_number.reverse()
    return binary_number


s = 0

for group_index, spring_group in enumerate(spring_groups):

    all_damaged = []
    for i in range(5):
        for damaged in spring_group["damaged"]:
            all_damaged.append(damaged)

    one_damaged = spring_group["damaged"]

    springs = spring_group["springs"]


    # First iteration
    springs_1 = springs.copy()
    springs_1.append("?")

    unknown_count = 0
    for spring in springs_1:
        if spring == "?":
            unknown_count += 1

    combination_count = 2 ** unknown_count

    possible_orders = {}

    for combination in range(combination_count):
        broken_list = get_binary_list(combination, unknown_count)
        
        new_springs = []
        broken_index = 0
        for spring in springs_1:
            if spring == "?":
                if broken_list[broken_index] == 0:
                    new_springs.append(".")
                else:
                    new_springs.append("#")
                broken_index += 1
            else:
                new_springs.append(spring)

        new_damaged = [0]
        for spring in new_springs:
            if spring == "#":
                new_damaged[-1] += 1
            else:
                if new_damaged[-1] != 0:
                    new_damaged.append(0)

        if new_damaged[-1] == 0 and len(new_damaged) != len(one_damaged):
            new_damaged.pop(len(new_damaged) - 1)

        possible_order = True
        for i in range(len(one_damaged)):
            if i >= len(new_damaged):
                possible_order = False
                break
            if new_damaged[i] != one_damaged[i]:
                possible_order = False
                break

        if new_damaged != one_damaged and new_springs[-1] != "#":
            possible_order = False

        if new_damaged[-1] > one_damaged[-1]:
            possible_order = False

        if (new_damaged[-1], new_springs[-1]) in possible_orders and possible_order:
            possible_orders[(new_damaged[-1], new_springs[-1])] += 1
        elif possible_order:
            possible_orders[(new_damaged[-1], new_springs[-1])] = 1

    print(possible_orders)

    # Middle iterations 

    # Last iteration

    print("Spring group {} out of {} done".format(group_index + 1, len(spring_groups)))

print("Sum of all possible arrangements:", s)

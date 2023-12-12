spring_groups = []

input_file = open("input.txt", "r")

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
    unknown_count = 0
    for spring in spring_group["springs"]:
        if spring == "?":
            unknown_count += 1

    combination_count = 2 ** unknown_count

    correct_orders = 0

    for combination in range(combination_count):
        broken_list = get_binary_list(combination, unknown_count)
        
        new_springs = []
        broken_index = 0
        for spring in spring_group["springs"]:
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

        if new_damaged[-1] == 0:
            new_damaged.pop(len(new_damaged) - 1)

        if new_damaged == spring_group["damaged"]:
            correct_orders += 1

    s += correct_orders

    print("Spring group {} out of {} done".format(group_index + 1, len(spring_groups)))


print("Sum of all possible arrangements:", s)

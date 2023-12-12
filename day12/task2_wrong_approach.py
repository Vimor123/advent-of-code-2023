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
    chosen_springs = spring_group["springs"]

    chosen_springs_1 = chosen_springs.copy()
    chosen_springs_2 = chosen_springs.copy()
    chosen_springs_3 = chosen_springs.copy()

    chosen_springs_1.append("?")
    chosen_springs_2.insert(0, "?")
    chosen_springs_2.append("?")
    chosen_springs_3.insert(0, "?")

    correct_orders = { 1 : { "." : 0, "#" : 0 },
                       2 : { (".", ".") : 0,
                             (".", "#") : 0,
                             ("#", ".") : 0,
                             ("#", "#") : 0 }, 
                       3 : { "." : 0, "#" : 0 }}

    for current_chosen_springs in [chosen_springs_1, chosen_springs_2, chosen_springs_3]:

        unknown_count = 0
        for spring in current_chosen_springs:
            if spring == "?":
                unknown_count += 1

        combination_count = 2 ** unknown_count

        for combination in range(combination_count):
            broken_list = get_binary_list(combination, unknown_count)
        
            new_springs = []
            broken_index = 0
            for spring in current_chosen_springs:
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
                if current_chosen_springs == chosen_springs_1:
                    correct_orders[1][new_springs[-1]] += 1
                elif current_chosen_springs == chosen_springs_2:
                    correct_orders[2][(new_springs[0], new_springs[-1])] += 1
                else:
                    correct_orders[3][new_springs[0]] += 1

    last_index_correct_orders = { "." : correct_orders[1]["."], "#" : correct_orders[1]["#"] }
    for i in range(3):
        new_correct_orders_1 = last_index_correct_orders["."] * correct_orders[2][(".", ".")] + last_index_correct_orders["#"] * correct_orders[2][("#", ".")]
        new_correct_orders_2 = last_index_correct_orders["."] * correct_orders[2][(".", "#")] + last_index_correct_orders["#"] * correct_orders[2][("#", "#")]

        last_index_correct_orders["."] = new_correct_orders_1
        last_index_correct_orders["#"] = new_correct_orders_2
    last_index_correct_orders["."] *= correct_orders[3]["."]
    last_index_correct_orders["#"] *= correct_orders[3]["#"]

    final_correct_orders = last_index_correct_orders["."] + last_index_correct_orders["#"]
    s += final_correct_orders

    print("Spring group {} out of {} done, {} correct arrangements".format(group_index + 1, len(spring_groups), final_correct_orders))


print("Sum of all possible arrangements:", s)

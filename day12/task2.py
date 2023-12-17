spring_groups = []

input_file = open("input.txt", "r")

for line in input_file:
    springs_1 = list(line.split()[0])
    springs = []
    for i in range(4):
        for spring in springs_1:
            springs.append(spring)
        springs.append("?")
    for spring in springs_1:
        springs.append(spring)
    damaged_groups = [int(x) for x in line.strip().split()[1].split(",")] * 5
    spring_groups.append({ "springs" : springs, "damaged" : damaged_groups })

input_file.close()


def spring_check(spring_group, spring_index, block_index, current_block_count):
    data_key = (spring_index, block_index, current_block_count)

    if data_key in data_table:
        return data_table[data_key]
    
    if spring_index == len(spring_group["springs"]):
        if block_index == len(spring_group["damaged"]) and current_block_count == 0:
            return 1
        elif block_index == len(spring_group["damaged"]) - 1 and current_block_count == spring_group["damaged"][-1]:
            return 1
        else:
            return 0

    valid_arrangements = 0
    for spring in [".", "#"]:
        if spring_group["springs"][spring_index] == spring or spring_group["springs"][spring_index] == "?":
            if spring == "." and current_block_count == 0:
                valid_arrangements += spring_check(spring_group, spring_index + 1, block_index, 0)
            elif spring == "." and current_block_count > 0 and block_index < len(spring_group["damaged"]) and current_block_count == spring_group["damaged"][block_index]:
                valid_arrangements += spring_check(spring_group, spring_index + 1, block_index + 1, 0)
            elif spring == "#":
                valid_arrangements += spring_check(spring_group, spring_index + 1, block_index, current_block_count + 1)

    data_table[data_key] = valid_arrangements
    return valid_arrangements     

s = 0

for spring_group in spring_groups:
    data_table = {}
    s += spring_check(spring_group, 0, 0, 0)

print(s)

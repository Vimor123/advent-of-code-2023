input_file = open("input.txt", "r")

seed_ranges = []
maps = {}

current_map = ""
reading_map = False

for line in input_file:
    if line.startswith("seeds:"):
        numbers = [int(x) for x in line[6:].strip().split()]
        no_of_ranges = len(numbers) // 2
        for i in range(no_of_ranges):
            seed_ranges.append((numbers[2 * i], numbers[2 * i] + numbers[2 * i + 1] - 1))
    elif line.strip().endswith("map:"):
        current_map = line.strip().split()[0]
        maps[current_map] = []
        reading_map = True
    elif line.strip() == "":
        reading_map = False
    elif reading_map:
        numbers = [int(x) for x in line.strip().split()]
        maps[current_map].append({ "source" : numbers[1],
                                   "destination" : numbers[0],
                                   "length" : numbers[2] })

input_file.close()


path_found = False
path = []
current_element = "location"

map_destinations = {}
for map_name in list(maps.keys()):
    map_destinations[map_name.split('-')[2]] = map_name

while not path_found:
    next_map = map_destinations[current_element]
    path.append(next_map)
    current_element = next_map.split('-')[0]

    if current_element == "seed":
        path_found = True

path.reverse()


current_ranges = seed_ranges.copy()

for conversion in path:
    mapping = maps[conversion]

    next_ranges = []

    for current_range in current_ranges:
        range_now = current_range
        for mapping_range in mapping:
            if range_now[1] < mapping_range["source"]:
                pass
            elif range_now[0] > mapping_range["source"] + mapping_range["length"] - 1:
                pass
            elif range_now[0] >= mapping_range["source"] and range_now[1] <= mapping_range["source"] + mapping_range["length"] - 1:
                next_ranges.append((mapping_range["destination"] + (range_now[0] - mapping_range["source"]), mapping_range["destination"] + (range_now[1] - mapping_range["source"])))
                range_now = (0, -1)
                break
            elif range_now[0] >= mapping_range["source"]:
                new_range = (mapping_range["destination"] + (range_now[0] - mapping_range["source"]), mapping_range["destination"] + mapping_range["length"] - 1)
                next_ranges.append(new_range)
                range_now = (mapping_range["source"] + mapping_range["length"], range_now[1])
            else:
                new_range = (mapping_range["destination"], mapping_range["destination"] + (range_now[1] - mapping_range["source"]))
                next_ranges.append(new_range)
                range_now = (range_now[0], mapping_range["source"] - 1)

        if range_now[0] <= range_now[1]:
            next_ranges.append(range_now)

    next_ranges = sorted(next_ranges, key = lambda next_range: next_range[0])

    ranges_minimal = False
    current_index = 0

    while not ranges_minimal:
        if current_index + 1 >= len(next_ranges):
            ranges_minimal = True
        else:
            if next_ranges[current_index][1] + 1 >= next_ranges[current_index + 1][0]:
                lost_range = next_ranges.pop(current_index + 1)
                next_ranges[current_index] = (next_ranges[current_index][0], max(next_ranges[current_index][1], lost_range[1]))
            else:
                current_index += 1

    current_ranges = next_ranges

print(current_ranges[0][0])

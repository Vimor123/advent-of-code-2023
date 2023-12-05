input_file = open("input.txt", "r")

seeds = []
maps = {}

current_map = ""
reading_map = False

for line in input_file:
    if line.startswith("seeds:"):
        seeds = [int(x) for x in line[6:].strip().split()]
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


locations = []

for seed in seeds:
    number = seed
    for conversion in path:
        mapping = maps[conversion]

        number_in_mapping_range = False

        for mapping_range in mapping:
            if number >= mapping_range["source"] and number < mapping_range["source"] + mapping_range["length"]:
                number = mapping_range["destination"] + (number - mapping_range["source"])
                break

    locations.append(number)

print(min(locations))

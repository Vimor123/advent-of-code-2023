import math

races = []

input_file = open("input.txt", "r")

times = []
distances = []

for line in input_file:
    if line.startswith("Time:"):
        times = [int(x) for x in line[5:].strip().split()]
    elif line.startswith("Distance:"):
        distances = [int(x) for x in line[9:].strip().split()]

for i in range(len(times)):
    races.append({"time" : times[i], "distance" : distances[i]})

input_file.close()


# x = time spent holding the button
# distance = (time - x) * x = - x ** 2 + time * x
# - x ** 2 + time * x - record = 0
# nullpoints = ( -time +- sqrt(time ** 2 - 4 * -1 * -record) ) / (2 * -1)

s = 1

for race in races:
    d = math.sqrt(race["time"] ** 2 - 4 * race["distance"])
    x1 = (race["time"] - d) / 2
    x2 = (race["time"] + d) / 2

    if x1 % 1 == 0:
        x1 += 0.1
    if x2 % 1 == 0:
        x2 -= 0.1
    
    low = math.ceil(x1)
    high = math.floor(x2)

    no_of_ways = high - low + 1
    s *= no_of_ways

print(s)

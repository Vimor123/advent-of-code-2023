import math

input_file = open("input.txt", "r")

times = []
distances = []

for line in input_file:
    if line.startswith("Time:"):
        times = line[5:].strip().split()
    elif line.startswith("Distance:"):
        distances = line[9:].strip().split()

input_file.close()

time = int("".join(times))
distance = int("".join(distances))

# x = time spent holding the button
# distance = (time - x) * x = - x ** 2 + time * x
# - x ** 2 + time * x - record = 0
# nullpoints = ( -time +- sqrt(time ** 2 - 4 * -1 * -record) ) / (2 * -1)

d = math.sqrt(time ** 2 - 4 * distance)
x1 = (time - d) / 2
x2 = (time + d) / 2

if x1 % 1 == 0:
    x1 += 0.1
if x2 % 1 == 0:
    x2 -= 0.1

no_of_ways = math.floor(x2) - math.ceil(x1) + 1 
print(no_of_ways)

# Credit: HyperNeutrino

import sympy

hailstones = []

input_file = open("input.txt", "r")

for line in input_file:
    position, velocity = line.strip().split(" @ ")
    position = tuple([int(x) for x in position.split(", ")])
    velocity = tuple([int(x) for x in velocity.split(", ")])
    hailstones.append({"position" : position, "velocity" : velocity})

input_file.close()


p_x, p_y, p_z, v_x, v_y, v_z = sympy.symbols("p_x, p_y, p_z, v_x, v_y, v_z")

equations = []

for hailstone in hailstones:

    equations.append((p_x - hailstone["position"][0]) * (hailstone["velocity"][1] - v_y) - (p_y - hailstone["position"][1]) * (hailstone["velocity"][0] - v_x))
    equations.append((p_y - hailstone["position"][1]) * (hailstone["velocity"][2] - v_z) - (p_z - hailstone["position"][2]) * (hailstone["velocity"][1] - v_y))

answer = sympy.solve(equations)[0]
print(answer[p_x] + answer[p_y] + answer[p_z])

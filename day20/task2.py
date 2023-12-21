# Credit : Jonathan Paulson

import math

modules = {}

input_file = open("input.txt", "r")

for line in input_file:
    module_string, neighbours_string = line.strip().split(" -> ")

    module_name = ""
    module = {}

    module["neighbours"] = neighbours_string.split(", ")
    module["predecessors"] = []

    if module_string.startswith("%"):
        module["type"] = "%"
        module_name = module_string[1:]
        module["state"] = False
    elif module_string.startswith("&"):
        module["type"] = "&"
        module_name = module_string[1:]
        module["inputs"] = {}
    else:
        module["type"] = "b"
        module_name = module_string

    modules[module_name] = module

input_file.close()


for module_name in modules:
    for module_neighbour_name in modules[module_name]["neighbours"]:
        if module_neighbour_name in modules:
            if modules[module_neighbour_name]["type"] == "&":
                modules[module_neighbour_name]["inputs"][module_name] = False
        if module_neighbour_name in modules:
            modules[module_neighbour_name]["predecessors"].append(module_name)


# sends to "rx" : "lb"
# "lb" is "&" : all predecessors' last signal pulses need to be high
# sends to "lb" : "rz", "lf", "br", "fk"


def lcm(numbers):
    multiple = 1
    for number in numbers:
        multiple = (multiple * number) // math.gcd(multiple, number)
    return multiple


key_modules = ["rz", "lf", "br", "fk"]

previous = {}
count = {}
cycle_lengths = []
low_signal_received = False
times_button_pushed = 0


while not low_signal_received:

    times_button_pushed += 1
    signals = [{"pulse_high" : False, "to" : "broadcaster"}]

    while len(signals) > 0:
        signal = signals.pop(0)

        if not signal["pulse_high"]:
            if signal["to"] in previous and signal["to"] in count and signal["to"] in key_modules:
                cycle_lengths.append(times_button_pushed - previous[signal["to"]])
            previous[signal["to"]] = times_button_pushed
            if signal["to"] in count:
                count[signal["to"]] += 1
            else:
                count[signal["to"]] = 1

        if len(cycle_lengths) == len(key_modules):
            print(lcm(cycle_lengths))
            low_signal_received = True
            break

        if signal["to"] not in modules:
            continue

        module = modules[signal["to"]]

        if module["type"] == "%":
            if not signal["pulse_high"]:
                module["state"] = not module["state"]
                for neighbour_module_name in module["neighbours"]:
                    signals.append({"pulse_high" : module["state"], "to" : neighbour_module_name})
                    if neighbour_module_name not in modules:
                        pass
                    elif modules[neighbour_module_name]["type"] == "&":
                        modules[neighbour_module_name]["inputs"][signal["to"]] = module["state"]
    
        elif module["type"] == "&":
            all_high = True
            for value in module["inputs"].values():
                if value == False:
                    all_high = False

            for neighbour_module_name in module["neighbours"]:
                signals.append({"pulse_high" : not all_high, "to" : neighbour_module_name})
                if neighbour_module_name not in modules:
                    pass
                elif modules[neighbour_module_name]["type"] == "&":
                    modules[neighbour_module_name]["inputs"][signal["to"]] = not all_high

        else:
            for neighbour_module_name in module["neighbours"]:
                signals.append({"pulse_high" : signal["pulse_high"], "to" : neighbour_module_name})
                if neighbour_module_name not in modules:
                    pass
                elif modules[neighbour_module_name]["type"] == "&":
                    modules[neighbour_module_name]["inputs"][signal["to"]] = signal["pulse_high"]

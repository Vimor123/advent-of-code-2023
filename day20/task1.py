modules = {}

input_file = open("input.txt", "r")

for line in input_file:
    module_string, neighbours_string = line.strip().split(" -> ")

    module_name = ""
    module = {}

    module["neighbours"] = neighbours_string.split(", ")

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


low_pulses = 0
high_pulses = 0

cycle_length = 0
cycle_detected = False
times_button_pushed = 0


while times_button_pushed < 1000:

    times_button_pushed += 1
    if not cycle_detected:
        cycle_length += 1
    signals = [{"pulse_high" : False, "to" : "broadcaster"}]

    while len(signals) > 0:
        signal = signals.pop(0)
    
        if signal["pulse_high"]:
            high_pulses += 1
        else:
            low_pulses += 1

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

    configuration_as_started = True
    for module in modules.values():
        if module["type"] == "%":
            if module["state"]:
                configuration_as_started = False
        elif module["type"] == "&":
            for value in module["inputs"].values():
                if value:
                    configuration_as_started = False
                    break

        if not configuration_as_started:
            break

    if configuration_as_started and not cycle_detected:
        cycle_detected = True
        no_of_cycles = 1000 // cycle_length
        low_pulses *= no_of_cycles
        high_pulses *= no_of_cycles
        times_button_pushed = no_of_cycles * cycle_length


print(low_pulses * high_pulses)

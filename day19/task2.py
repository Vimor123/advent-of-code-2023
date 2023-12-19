workflows = {}

parts = []


input_file = open("input.txt", "r")

reading_workflows = True

for line in input_file:
    if line.strip() == "":
        reading_workflows = False
    elif reading_workflows:
        name = line[:line.index("{")]
        rules = line[line.index("{") + 1:line.index("}")].split(",")
        formatted_rules = []
        for i in range(len(rules) - 1):
            condition_string, destination = rules[i].split(":")
            if ">" in condition_string:
                condition = {"category" : condition_string.split(">")[0],
                             "operation" : ">",
                             "value" : int(condition_string.split(">")[1])}
            else:
                condition = {"category" : condition_string.split("<")[0],
                             "operation" : "<",
                             "value" : int(condition_string.split("<")[1])}

            formatted_rules.append({"condition" : condition, "destination" : destination})
        formatted_rules.append({"condition" : None, "destination" : rules[-1]})
        workflows[name] = formatted_rules

input_file.close()


def accepted_combinations(workflow_name, legal_ranges):
    if workflow_name == "A":
        combinations = 1
        for legal_range in legal_ranges.values():
            combinations *= legal_range[1] - legal_range[0] + 1
        return combinations
    elif workflow_name == "R":
        return 0

    combinations = 0
    workflow = workflows[workflow_name]
    for rule in workflow:
        if rule["condition"] == None:
            combinations += accepted_combinations(rule["destination"], legal_ranges)
        else:
            selected_category = rule["condition"]["category"]
            legal_range = legal_ranges[selected_category]
            value = rule["condition"]["value"]
            if rule["condition"]["operation"] == ">":
                if legal_range[0] > value:
                    combinations += accepted_combinations(rule["destination"], legal_ranges)
                    break
                elif legal_range[1] > value:
                    new_legal_ranges = {}
                    for category, legal_range in legal_ranges.items():
                        new_legal_ranges[category] = legal_range
                    new_legal_ranges[selected_category] = (value + 1, new_legal_ranges[selected_category][1])
                    combinations += accepted_combinations(rule["destination"], new_legal_ranges)
                    legal_ranges[selected_category] = (legal_ranges[selected_category][0], value)
            else:
                if legal_range[1] < value:
                    combinations += accepted_combinations(rule["destination"], legal_ranges)
                    break
                elif legal_range[0] < value:
                    new_legal_ranges = {}
                    for category, legal_range in legal_ranges.items():
                        new_legal_ranges[category] = legal_range
                    new_legal_ranges[selected_category] = (new_legal_ranges[selected_category][0], value - 1)
                    combinations += accepted_combinations(rule["destination"], new_legal_ranges)
                    legal_ranges[selected_category] = (value, legal_ranges[selected_category][1])
    
    return combinations


starting_workflow_name = "in"
starting_legal_ranges = {"x" : (1, 4000),
                         "m" : (1, 4000),
                         "a" : (1, 4000),
                         "s" : (1, 4000)}

print(accepted_combinations(starting_workflow_name, starting_legal_ranges))

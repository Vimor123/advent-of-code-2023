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

    else:
        new_part = {}
        category_strings = line.strip()[1:-1].split(",")
        for category_string in category_strings:
            new_part[category_string.split("=")[0]] = int(category_string.split("=")[1])
        parts.append(new_part)

input_file.close()


s = 0

for part in parts:
    workflow_name = "in"
    accepted = False
    processing_finished = False
    while not processing_finished:
        workflow = workflows[workflow_name]
        for rule in workflow:
            if rule["condition"] == None:
                new_workflow_name = rule["destination"]
                break
            else:
                if rule["condition"]["operation"] == ">":
                    if part[rule["condition"]["category"]] > rule["condition"]["value"]:
                        new_workflow_name = rule["destination"]
                        break
                else:
                    if part[rule["condition"]["category"]] < rule["condition"]["value"]:
                        new_workflow_name = rule["destination"]
                        break

        if new_workflow_name == "A" or new_workflow_name == "R":
            if new_workflow_name == "A":
                accepted = True
            processing_finished = True
        
        workflow_name = new_workflow_name

    if accepted:
        s += sum(part.values())

print(s)

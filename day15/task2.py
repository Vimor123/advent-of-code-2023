def hash(word):
    hash_value = 0
    for character in word:
        hash_value += ord(character)
        hash_value *= 17
        hash_value %= 256
    return hash_value


input_file = open("input.txt", "r")

step_strings = input_file.readline().strip().split(",")

input_file.close()


boxes = {}

for step_string in step_strings:
    if step_string.endswith("-"):
        label = step_string[:-1]
        box_number = hash(label)
        if box_number in boxes:
            for i in range(len(boxes[box_number])):
                if boxes[box_number][i][0] == label:
                    boxes[box_number].pop(i)
                    break
    else:
        label = step_string.split("=")[0]
        focal_length = int(step_string.split("=")[1])
        box_number = hash(label)
        if box_number in boxes:
            label_present = False
            for i in range(len(boxes[box_number])):
                if boxes[box_number][i][0] == label:
                    label_present = True
                    boxes[box_number][i] = (label, focal_length)
                    break
            if not label_present:
                boxes[box_number].append((label, focal_length))
        else:
            boxes[box_number] = [(label, focal_length)]


focusing_power = 0

for box_number, box in boxes.items():
    for lens_index, lens in enumerate(box):
        focusing_power += (box_number + 1) * (lens_index + 1) * lens[1]

print(focusing_power)

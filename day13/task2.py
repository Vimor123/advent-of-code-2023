patterns = [[]]

input_file = open("input.txt", "r")

for line in input_file:
    if line.strip() != "":
        patterns[-1].append(list(line.strip()))
    else:
        patterns.append([])

input_file.close()


def matching_rows(pattern, row_index_1, row_index_2):
    if pattern[row_index_1] == pattern[row_index_2]:
        return True
    return False


def matching_columns(pattern, column_index_1, column_index_2):
    for i in range(len(pattern)):
        if pattern[i][column_index_1] != pattern[i][column_index_2]:
            return False
    return True


previous_reflections = []

for pattern in patterns:

    score = 0

    reflection_found = False

    for row_index in range(1, len(pattern)):
        left_end = row_index - 1
        right_end = row_index

        reflection = True
        while left_end >= 0 and right_end < len(pattern):
            if not matching_rows(pattern, left_end, right_end):
                reflection = False
            left_end -= 1
            right_end += 1

        if reflection:
            score += row_index * 100
            reflection_found = True
            previous_reflections.append(("row", row_index))
            break

    if reflection_found:
        continue

    for column_index in range(1, len(pattern[0])):
        left_end = column_index - 1
        right_end = column_index

        reflection = True
        while left_end >= 0 and right_end < len(pattern[0]):
            if not matching_columns(pattern, left_end, right_end):
                reflection = False
            left_end -= 1
            right_end += 1

        if reflection:
            score += column_index
            previous_reflections.append(("column", column_index))
            break
    

s = 0

for pattern, previous_reflection in zip(patterns, previous_reflections):

    smudge_found = False

    new_score = 0

    for i in range(len(pattern)):
        for j in range(len(pattern[0])):
            new_pattern = []
            for row in pattern:
                new_pattern.append(row.copy())

            if new_pattern[i][j] == "#":
                new_pattern[i][j] = "."
            else:
                new_pattern[i][j] = "#"


            for row_index in range(1, len(pattern)):
                left_end = row_index - 1
                right_end = row_index

                reflection = True
                while left_end >= 0 and right_end < len(pattern):
                    if not matching_rows(new_pattern, left_end, right_end):
                        reflection = False
                    left_end -= 1
                    right_end += 1

                if reflection:
                    if previous_reflection[0] != "row" or previous_reflection[1] != row_index:
                        smudge_found = True
                        new_score = row_index * 100
                        break

            if smudge_found:
                break

            for column_index in range(1, len(pattern[0])):
                left_end = column_index - 1
                right_end = column_index

                reflection = True
                while left_end >= 0 and right_end < len(pattern[0]):
                    if not matching_columns(new_pattern, left_end, right_end):
                        reflection = False
                    left_end -= 1
                    right_end += 1

                if reflection:
                    if previous_reflection[0] != "column" or previous_reflection[1] != column_index:
                        smudge_found = True
                        new_score = column_index
                        break

        if smudge_found:
            break
    
    s += new_score

print(s)

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


s = 0

for pattern in patterns:
    score = 0

    """
    for row_index in range(1, len(pattern) - 1):
        middle = row_index
        left_end = middle - 1
        right_end = middle + 1

        reflection = True
        while left_end >= 0 and right_end < len(pattern):
            if not matching_rows(pattern, left_end, right_end):
                reflection = False
                break
            left_end -= 1
            right_end += 1

        if reflection:
            score += middle * 100
            print("hit")
            print(middle)
            for row in pattern:
                print("".join(row))
    """

    for row_index in range(1, len(pattern)):
        left_end = row_index - 1
        right_end = row_index

        reflection = True
        while left_end >= 0 and right_end < len(pattern):
            if not matching_rows(pattern, left_end, right_end):
                reflection = False
                break
            left_end -= 1
            right_end += 1

        if reflection:
            score += row_index * 100

    """
    for column_index in range(1, len(pattern[0]) - 1):
        middle = column_index
        left_end = middle - 1
        right_end = middle + 1

        reflection = True
        while left_end >= 0 and right_end < len(pattern[0]):
            if not matching_columns(pattern, left_end, right_end):
                reflection = False
                break
            left_end -= 1
            right_end += 1

        if reflection:
            score += middle
    """

    for column_index in range(1, len(pattern[0])):
        left_end = column_index - 1
        right_end = column_index

        reflection = True
        while left_end >= 0 and right_end < len(pattern[0]):
            if not matching_columns(pattern, left_end, right_end):
                reflection = False
                break
            left_end -= 1
            right_end += 1

        if reflection:
            score += column_index

    s += score

print(s)

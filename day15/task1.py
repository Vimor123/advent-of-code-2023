def hash(word):
    hash_value = 0
    for character in word:
        hash_value += ord(character)
        hash_value *= 17
        hash_value %= 256
    return hash_value


input_file = open("input.txt", "r")

sequence = input_file.readline().strip().split(",")

input_file.close()

s = 0

for word in sequence:
    s += hash(word)

print(s)

numbers = []

inputFile = open("input.txt", "r")

for line in inputFile:
    firstDigit = -1
    lastDigit = -1
    for character in line:
        if character.isnumeric():
            lastDigit = character
            if firstDigit == -1:
                firstDigit = character
    numbers.append(int(firstDigit + lastDigit))

print(sum(numbers))

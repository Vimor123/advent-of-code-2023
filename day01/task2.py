numbers = []

inputFile = open("input.txt", "r")

for line in inputFile:
    firstDigit = 0
    lastDigit = 0
    for char_index, character in enumerate(line):
        if character.isnumeric():
            lastDigit = character
            if firstDigit == 0:
                firstDigit = character
        else:
            if character == "o" and char_index + 2 < len(line):
                if line[char_index: char_index + 3] == "one":
                    lastDigit = "1"
                    if firstDigit == 0:
                        firstDigit = "1"

            if character == "t" and char_index + 2 < len(line):
                if line[char_index: char_index + 3] == "two":
                    lastDigit = "2"
                    if firstDigit == 0:
                        firstDigit = "2"

            if character == "t" and char_index + 4 < len(line):
                if line[char_index: char_index + 5] == "three":
                    lastDigit = "3"
                    if firstDigit == 0:
                        firstDigit = "3"

            if character == "f" and char_index + 3 < len(line):
                if line[char_index: char_index + 4] == "four":
                    lastDigit = "4"
                    if firstDigit == 0:
                        firstDigit = "4"

            if character == "f" and char_index + 3 < len(line):
                if line[char_index: char_index + 4] == "five":
                    lastDigit = "5"
                    if firstDigit == 0:
                        firstDigit = "5"

            if character == "s" and char_index + 2 < len(line):
                if line[char_index: char_index + 3] == "six":
                    lastDigit = "6"
                    if firstDigit == 0:
                        firstDigit = "6"
            
            if character == "s" and char_index + 4 < len(line):
                if line[char_index: char_index + 5] == "seven":
                    lastDigit = "7"
                    if firstDigit == 0:
                        firstDigit = "7"

            if character == "e" and char_index + 4 < len(line):
                if line[char_index: char_index + 5] == "eight":
                    lastDigit = "8"
                    if firstDigit == 0:
                        firstDigit = "8"

            if character == "n" and char_index + 3 < len(line):
                if line[char_index: char_index + 4] == "nine":
                    lastDigit = "9"
                    if firstDigit == 0:
                        firstDigit = "9"
    
    numbers.append(int(firstDigit + lastDigit))

print(sum(numbers))

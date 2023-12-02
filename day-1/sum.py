#!/usr/bin/env python3

input_doc = open("input", "r")
total = 0

for line in input_doc:
    new_line = ""
    position = 0

    while position < len(line):
        if line[position].isdigit():
            new_line += line[position]
        elif line[position:position + 3] == "one":
            new_line += "1"
        elif line[position:position + 3] == "two":
            new_line += "2"
        elif line[position:position + 5] == "three":
            new_line += "3"
        elif line[position:position + 4] == "four":
            new_line += "4"
        elif line[position:position + 4] == "five":
            new_line += "5"
        elif line[position:position + 3] == "six":
            new_line += "6"
        elif line[position:position + 5] == "seven":
            new_line += "7"
        elif line[position:position + 5] == "eight":
            new_line += "8"
        elif line[position:position + 4] == "nine":
            new_line += "9"

        position += 1

    total += int(new_line[0] + new_line[-1])
print(total)
#    for char in reversed(line):
#        if char.isdigit():
#            second = char
#            break
#
#    total += int(first + second)
#print(new_line)

input_doc.close()

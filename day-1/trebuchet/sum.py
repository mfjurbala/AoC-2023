#!/usr/bin/env python3

input_doc = open("input", "r")
total = 0

for line in input_doc:

    for char in line:
        if char.isdigit():
            first = char
            break

    for char in reversed(line):
        if char.isdigit():
            second = char
            break

    total += int(first + second)

print(total)

input_doc.close()

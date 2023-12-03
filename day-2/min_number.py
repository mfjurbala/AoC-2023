#!/usr/bin/env python3

game_count = 1
total = 0

for line in open("input", "r"):
    max_red = 1
    max_green = 1
    max_blue = 1

    for game in line.rstrip("\n").split(": ")[1].split("; "):

        dictionary = dict(pull.split(" ")[::-1] for pull in game.split(", "))
        print(dictionary)

        if "red" in dictionary and int(dictionary["red"]) > max_red:
            max_red = int(dictionary["red"])

        if "green" in dictionary and int(dictionary["green"]) > max_green:
            max_green = int(dictionary["green"])

        if "blue" in dictionary and int(dictionary["blue"]) > max_blue:
            max_blue = int(dictionary["blue"])

    power = max_red * max_green * max_blue
    total += power
    game_count += 1

print(total)

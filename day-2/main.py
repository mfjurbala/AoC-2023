#!/usr/bin/env python3

#This is semi-intentionally convoluted. It seemed funny at the time,
#might come back and try to make it better.

game_count = 1
total = 0

for line in open("input", "r"):
    skip = False

    for game in line.rstrip("\n").split(": ")[1].split("; "):
        dictionary = dict(pull.split(" ") for pull in game.split(", "))
        correct_dictionary = dict(zip(dictionary.values(), dictionary.keys()))

        if "red" in correct_dictionary and int(correct_dictionary["red"]) > 12:
            skip = True
        elif "green" in correct_dictionary and int(correct_dictionary["green"]) > 13:
            skip = True
        elif "blue" in correct_dictionary and int(correct_dictionary["blue"]) > 14:
            skip = True

    if not skip:
        total += game_count
        print(game_count)

    game_count += 1

print(total)

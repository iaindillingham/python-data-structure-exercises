import sys

# This program knows about the RGB code corresponding to common colours.
#
# Usage:
#
# $ python rgb_colours.py [colour]
#
# For instance:
#
# $ python rgb_colours.py red
# The RGB code for red is F00
#
# or:
#
# $ python rgb_colours.py "burnt sienna"
# I don't know the RGB code for burnt sienna

colours = [
    ["red", "f00"],
    ["yellow", "ff0"],
    ["green", "0f0"],
    ["cyan", "0ff"],
    ["blue", "00f"],
    ["magenta", "f0f"],
]


def main(key):
    index = dict(colours) | dict(c[::-1] for c in colours)
    value = index.get(key)
    if value is None:
        print(f"I don't have an entry for {key}")
    else:
        print(f"The entry for {key} is {value}")


if __name__ == "__main__":
    main(sys.argv[1].lower())


# TODO:
# * Implement the program as described in the comments at the top of the file.

# TODO (extra):
# * Change the program so that users can also enter an RGB colour code, and be
#   told the name of the corresponding colour.
# * Change the program so that it ignores the case of the user's input.

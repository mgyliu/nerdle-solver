import time
from random import sample
import os
import pdb

from constants import LENGTH, EXPRS_FILENAME
from generate import *


def validHints(hints):
    # it should be the right length
    # it should contain the right letters
    return (len(hints) == LENGTH) and (
        set(list(hints)) - set(["G", "P", "B"]) == set([])
    )


def getNextGuess(curr_guess, hints, exprs):
    # make a dict like this
    # {
    #     "*": [("G", 1)]                     present in this position
    #     "6": [("B", j), ("P", i)]           present once more, not in j and not in i
    #     "7": [("B", j), ("P", i), ("P", k)] present 2 times more, not in j and not in i and not in k
    #     "9": [("B", j)]                     not present
    #     "1": [("P", j)]                     present once more, not in j
    # }

    hint_map = {}
    for i in range(len(curr_guess)):
        unit = curr_guess[i]
        hint = hints[i]

        if unit in hint_map:
            hint_map[unit].append((hint, i))
        else:
            hint_map[unit] = [(hint, i)]

    for unit in hint_map:
        hint_pairs = hint_map[unit]

        green_pairs = [pair for pair in hint_pairs if pair[0] == "G"]
        black_pairs = [pair for pair in hint_pairs if pair[0] == "B"]
        purple_pairs = [pair for pair in hint_pairs if pair[0] == "P"]

        for gpair in green_pairs:
            idx = gpair[1]
            exprs = list(filter(lambda x: x[idx] == unit, exprs))

        # tells us there are exactly len(purple_pairs) more of unit in the expr
        if len(purple_pairs) > 0 and len(black_pairs) > 0:
            for ppair in purple_pairs:
                idx = ppair[1]
                exprs = list(
                    filter(
                        lambda x: x[idx] != unit and x.count(unit) == len(purple_pairs),
                        exprs,
                    )
                )
            for bpair in black_pairs:
                idx = bpair[1]
                exprs = list(filter(lambda x: x[idx] != unit, exprs))
        else:
            # there are at least len(purple_pairs) more of unit left in the expr
            # we just know they're not at the specified position
            for ppair in purple_pairs:
                idx = ppair[1]
                exprs = list(filter(lambda x: x[idx] != unit and unit in x, exprs))
            # there are none of the black letters in the expr
            # already accounted for the repeated letter case
            for bpair in black_pairs:
                idx = bpair[1]
                exprs = list(filter(lambda x: unit not in x, exprs))

    return sample(exprs, 1)[0], exprs


def main():
    if os.path.exists(EXPRS_FILENAME):
        with open(EXPRS_FILENAME, "r") as f:
            exprs = [x.strip() for x in f.readlines() if len(x) > 0]
    else:
        exprs = generateValidEquations(LENGTH)

    # First guess should include unique numbers and operators
    first_guess_choices = [x for x in exprs if len(set(list(x))) == len(x)]
    curr_guess = sample(first_guess_choices, 1)[0]

    print("Input results using the letters G=Green, P=Purple, B=Black with no spaces.")
    done = False
    while not done:
        print("Current guess: " + curr_guess)
        hints = input("Result: ")

        if not validHints(hints):
            print("Hints not in the right format. Try again")
            continue

        if hints == "GGGGGGGG":
            print("Woohoo!")
            done = True
            continue

        curr_guess, exprs = getNextGuess(curr_guess, hints, exprs)


if __name__ == "__main__":
    main()

import os
from constants import LENGTH, EXPRS_FILENAME
from generate import *
from guess import *
import argparse


def parseArgs():
    parser = argparse.ArgumentParser(description="Solve Nerdle.")
    parser.add_argument("--from-guess", action="store_const", const=True)

    return parser.parse_args()


def main():
    args = parseArgs()
    from_guess = args.from_guess

    exprs = getExprs()

    if from_guess:
        curr_guess = input("Your guess: ")
    else:
        curr_guess = generateFirstGuess(exprs)

    print(
        'Input results using the letters G=Green, P=Purple, B=Black with no spaces. When done, input either all G\'s or the string "done"'
    )
    done = False
    while not done:
        print("Current guess: " + curr_guess)
        hints = input("Result: ")

        if not validHints(hints):
            print("Hints not in the right format. Try again")
            continue

        if hints == "G" * LENGTH or hints == "done":
            print("Woohoo!")
            done = True
            continue

        curr_guess, exprs = getNextGuess(curr_guess, hints, exprs)


if __name__ == "__main__":
    main()

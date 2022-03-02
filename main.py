import os
from constants import LENGTH, EXPRS_FILENAME
from generate import *
from guess import *


def main():
    exprs = getExprs()
    curr_guess = generateFirstGuess(exprs)

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

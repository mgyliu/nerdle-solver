from collections import Counter
from guess import *
from pprint import pprint

ANSWERS_COUNT = 100
ITERATIONS = 100


def getHints(answer, guess):
    matches = [i for i in range(0, len(answer)) if answer[i] == guess[i]]
    mismatch_answer = [
        answer[i] for i in range(0, len(answer)) if answer[i] != guess[i]
    ]
    mismatch_guess = [guess[i] for i in range(0, len(answer)) if answer[i] != guess[i]]

    mismatch_answer_d = dict(Counter(mismatch_answer))
    hint = ""
    for i in range(0, len(answer)):
        if i in matches:
            hint += "G"
        else:
            this_guess = mismatch_guess.pop(0)
            if this_guess in mismatch_answer:
                if mismatch_answer_d[this_guess] > 0:
                    hint += "P"
                    mismatch_answer_d[this_guess] -= 1
                else:
                    hint += "B"
            else:
                hint += "B"

    return hint


def runForAnswer(answer, exprs, n=ITERATIONS, length=LENGTH):
    result = []
    first_guess_choices = [x for x in exprs if len(set(list(x))) == len(x)]
    first_guesses = random.sample(first_guess_choices, n)

    for i in range(0, n):
        done = False
        iter_count = 0
        curr_guess = first_guesses.pop()

        while not done:
            iter_count += 1
            hints = getHints(answer, curr_guess)

            result.append(
                {
                    "run_idx": i,
                    "answer": answer,
                    "guess": curr_guess,
                    "hints": hints,
                    "iter": iter_count,
                }
            )
            if hints == "G" * LENGTH:
                done = True
                break
            curr_guess, exprs = getNextGuess(curr_guess, hints, exprs)
    return result


if __name__ == "__main__":
    result = runForAnswer("3*42=126", getExprs())

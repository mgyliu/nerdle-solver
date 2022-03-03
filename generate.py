from constants import *
from itertools import product
import re

from evaluate import evaluateExpression


def generateSyntaxValidExpressions(length):
    if length == 1:
        return NUMBERS
    elif length == 2:
        return ["".join(x) for x in product(NUMBERS_POS, NUMBERS)]
    else:
        final_list = []
        for i in range(1, length - 1):
            suffix_length = length - i - 1

            prefixes = generateSyntaxValidExpressions(i)
            suffixes = generateSyntaxValidExpressions(suffix_length)

            l1 = [
                "".join(x)
                for x in product(
                    prefixes,
                    OPERATORS_COMMUTATIVE + NUMBERS,
                    suffixes,
                )
            ]
            # ensure no division by zero
            l2 = [
                "".join(x)
                for x in product(
                    prefixes,
                    OPERATORS_DIV,
                    filter(lambda x: x != "0" * suffix_length, suffixes),
                )
            ]

            # filter out anything with leading zeroes
            # regex is None ==> no leading zeroes
            final_list += filter(
                lambda x: re.match(r"^(0+[0-9]+)", x) is None and "/0" not in x, l1 + l2
            )

        return final_list


def createEvalDict(expressions):
    d = {}
    for expr in expressions:
        value = evaluateExpression(expr)
        if value in d:
            d[value].append(expr)
        else:
            d[value] = [expr]
    return d


def generateValidEquations(length):
    assert length > 3

    exprs = []
    for i in range(1, length - 1):
        d1 = createEvalDict(generateSyntaxValidExpressions(i))
        d2 = createEvalDict(generateSyntaxValidExpressions(length - i - 1))

        values1 = set(d1.keys())
        values2 = set(d2.keys())

        overlap = values1.intersection(values2)

        for value in overlap:
            exprs += ["".join(x) for x in product(d1[value], RELATIONS, d2[value])]

    return exprs


def main():
    exprs = generateValidEquations(LENGTH)
    with open(EXPRS_FILENAME, "w") as f:
        f.write("\n".join(exprs))


if __name__ == "__main__":
    main()

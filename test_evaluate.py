import unittest
from evaluate import evaluateExpression


class TestEvaluate(unittest.TestCase):
    def test_add(self):
        self.assertEqual(evaluateExpression("1+2"), 1 + 2, "Addition works")

    def test_diff(self):
        self.assertEqual(evaluateExpression("5-3"), 5 - 3, "Subtraction works")

    def test_mult(self):
        self.assertEqual(evaluateExpression("5*3"), 5 * 3, "Multiplication works")

    def test_div(self):
        self.assertEqual(evaluateExpression("6/3"), 6 / 3, "Division works")

    def test_bedmas(self):
        self.assertEqual(
            evaluateExpression("6+6/3"), 6 + 6 / 3, "Order of operations is correct"
        )
        self.assertEqual(
            evaluateExpression("6+6/3-5"),
            6 + 6 / 3 - 5,
            "Order of operations is correct",
        )
        self.assertEqual(
            evaluateExpression("6/6-8/4"),
            6 / 6 - 8 / 4,
            "Order of operations is correct",
        )
        self.assertEqual(
            evaluateExpression("8/7/95"), 8.0 / 7 / 95, "Chained division works"
        )


if __name__ == "__main__":
    unittest.main()

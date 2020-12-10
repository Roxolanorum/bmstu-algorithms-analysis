import unittest
from matrices import *


class TestSorts(unittest.TestCase):
    def test_identity(self):
        a = [[i==j for i in range(5)] for j in range(5)]
        c = [[0 for i in range(5)] for j in range(5)]
        self.assertEqual(classic_multiply(a, a, c), a)
        self.assertEqual(winograd(a, a, c), a)
        self.assertEqual(optimised_winograd(a, a, c), a)

    def test_square(self):
        a = [[1, 2, 3], [3, 2, 1], [2, 3, 1]]
        b = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        res = [[14, 14, 14], [10, 10, 10], [11, 11, 11]]
        self.assertEqual(classic_multiply(a, b, c), res)
        c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(winograd(a, b, c), res)
        c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(optimised_winograd(a, b, c), res)

    def test_general_odd(self):
        a = [[3, 7, -2], [-11, 7, 3]]
        b = [[1, 0, 11], [-1, 7, 17], [2, 6, -14]]
        c = [[0, 0, 0], [0, 0, 0]]
        res = [[-8, 37, 180], [-12, 67, -44]]

        self.assertEqual(classic_multiply(a, b, c), res)

        c = [[0, 0, 0], [0, 0, 0]]
        self.assertEqual(winograd(a, b, c), res)

        c = [[0, 0, 0], [0, 0, 0]]
        self.assertEqual(optimised_winograd(a, b, c), res)

    def test_general_even(self):
        a = [[3, 7, -2, 0], [-11, 7, 3, 1]]
        b = [[1, 0, 11], [-1, 7, 17], [2, 6, -14], [-3, -4, -22]]
        c = [[0, 0, 0], [0, 0, 0]]
        res = [[-8, 37, 180], [-15, 63, -66]]

        self.assertEqual(classic_multiply(a, b, c), res)

        c = [[0, 0, 0], [0, 0, 0]]
        self.assertEqual(winograd(a, b, c), res)

        c = [[0, 0, 0], [0, 0, 0]]
        self.assertEqual(optimised_winograd(a, b, c), res)


if __name__ == "__main__":
    unittest.main()
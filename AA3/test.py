import unittest
from sorts import *


class TestSorts(unittest.TestCase):
    def test_sorted(self):
        self.assertEqual(bubble_sort([i for i in range(10)]), [i for i in range(10)])
        self.assertEqual(selection_sort([i for i in range(10)]), [i for i in range(10)])
        self.assertEqual(insertion_sort([i for i in range(10)]), [i for i in range(10)])

    def test_reverse_sorted(self):
        self.assertEqual(bubble_sort([i for i in range(9, -1, -1)]), [i for i in range(10)])
        self.assertEqual(selection_sort([i for i in range(9, -1, -1)]), [i for i in range(10)])
        self.assertEqual(insertion_sort([i for i in range(9, -1, -1)]), [i for i in range(10)])

    def test_general(self):
        arr = [2, 0, 1, 6, 4, 3, 9, 7, 5, 8]
        self.assertEqual(bubble_sort(arr), [i for i in range(10)])
        self.assertEqual(selection_sort(arr), [i for i in range(10)])
        self.assertEqual(insertion_sort(arr), [i for i in range(10)])


if __name__ == "__main__":
    unittest.main()
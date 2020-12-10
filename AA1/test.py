import unittest
from levenshtein import *


class TestLevenshtein(unittest.TestCase):
    def test_emptyfirst(self):
        self.assertEqual(levenshtein_matrix("", "teststring"), 10)
        self.assertEqual(levenshtein_rec_wrap("", "teststring"), 10)
        self.assertEqual(levenshtein_rec_matr_wrap("", "teststring"), 10)
        self.assertEqual(dameray_levenshtein("", "teststring"), 10)

    def test_emptysecond(self):
        self.assertEqual(levenshtein_matrix("notteststring", ""), 13)
        self.assertEqual(levenshtein_rec_wrap("notteststring", ""), 13)
        self.assertEqual(levenshtein_rec_matr_wrap("notteststring", ""), 13)
        self.assertEqual(dameray_levenshtein("notteststring", ""), 13)

    def test_equal(self):
        self.assertEqual(levenshtein_matrix("IAmEqualTo", "IAmEqualTo"), 0)
        self.assertEqual(levenshtein_rec_wrap("IAmEqualTo", "IAmEqualTo"), 0)
        self.assertEqual(levenshtein_rec_matr_wrap("IAmEqualTo", "IAmEqualTo"), 0)
        self.assertEqual(dameray_levenshtein("IAmEqualTo", "IAmEqualTo"), 0)

    def test_general1(self):
        self.assertEqual(levenshtein_matrix("telo", "stolb"), 3)
        self.assertEqual(levenshtein_rec_wrap("telo", "stolb"), 3)
        self.assertEqual(levenshtein_rec_matr_wrap("telo", "stolb"), 3)
        self.assertEqual(dameray_levenshtein("telo", "stolb"), 3)

    def test_general2(self):
        self.assertEqual(levenshtein_matrix("polynomial", "exponential"), 6)
        self.assertEqual(levenshtein_rec_wrap("polynomial", "exponential"), 6)
        self.assertEqual(levenshtein_rec_matr_wrap("polynomial", "exponential"), 6)
        self.assertEqual(dameray_levenshtein("polynomial", "exponential"), 6)

    def test_general3(self):
        self.assertEqual(levenshtein_matrix("abba", "abab"), 2)
        self.assertEqual(levenshtein_rec_wrap("abba", "abab"), 2)
        self.assertEqual(levenshtein_rec_matr_wrap("abba", "abab"), 2)
        self.assertEqual(dameray_levenshtein("abba", "abab"), 1)


if __name__ == "__main__":
    unittest.main()
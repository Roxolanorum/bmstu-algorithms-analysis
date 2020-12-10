import unittest
from search import *


class TestSorts(unittest.TestCase):
    def test_search(self):
        array = ['АРБУЗ', 'БАНАН', 'ВИНОГРАД', 'ГРУША', 'ДЫНЯ']

        for token in array:
            self.assertEqual(lsearch(array, token), True)
            self.assertEqual(bsearch_wrap(array, token), True)
            self.assertEqual(fsearch_wrap(array, token), True)

        self.assertEqual(lsearch(array, 'ВИНО'), False)
        self.assertEqual(bsearch_wrap(array, 'ВИНО'), False)
        self.assertEqual(fsearch_wrap(array, 'ВИНО'), False)


if __name__ == "__main__":
    unittest.main()
import unittest
from typing import List


def plusOne(digits: List[int]) -> List[int]:
    """
    :type digits: List[int]
    :rtype: List[int]
    """

    # TODO: Implement the solution here.

    pass


class PlusOneTestCase(unittest.TestCase):
    def test_1(self):
        digits = [1, 2, 3]
        expected = [1, 2, 4]
        result = plusOne(digits)
        self.assertListEqual(result, expected)

    def test_2(self):
        digits = [4, 3, 2, 1]
        expected = [4, 3, 2, 2]
        result = plusOne(digits)
        self.assertListEqual(result, expected)

    def test_3(self):
        digits = [9]
        expected = [1, 0]
        result = plusOne(digits)
        self.assertListEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
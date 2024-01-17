import unittest
from typing import List


def plusOne(digits: List[int]) -> List[int]:
    temp = ""
    l = []

    for digit in digits:
        temp += str(digit)

    temp = int(temp) + 1

    for char in str(temp):
        l.append(int(char))

    return l


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

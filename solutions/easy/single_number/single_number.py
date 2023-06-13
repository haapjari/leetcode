import unittest

def singleNumber(nums):
    def calcCount(list, val):
        c = 0
        for elem in list:
            if elem == val:
                c += 1
        return c

    for num in nums:
        if calcCount(nums, num) == 1:
            return num


class SingleNumberTestCase(unittest.TestCase):
    def test_1(self):
        nums = [2, 2, 1]
        expected = 1
        result = singleNumber(nums)
        self.assertEqual(result, expected)

    def test_2(self):
        nums = [4, 1, 2, 1, 2]
        expected = 4
        result = singleNumber(nums)
        self.assertEqual(result, expected)

    def test_3(self):
        nums = [1]
        expected = 1
        result = singleNumber(nums)
        self.assertEqual(result, expected)

    def test_4(self):
        nums = [5, 7, 5, 6, 6]
        expected = 7
        result = singleNumber(nums)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

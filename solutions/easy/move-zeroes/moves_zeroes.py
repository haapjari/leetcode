import unittest
from typing import List


def moveZeroes(nums: List[int]) -> List[int]:
    """
    Do not return anything, modify nums in-place instead.
    """

    i = len(nums) - 1
    while i >= 0:
        if nums[i] == 0:
            nums.append(nums.pop(i))

        i -= 1

    return nums

class PlusOneTestCase(unittest.TestCase):
    def test_1(self):
        nums = [0, 1, 0, 3, 12]
        expected = [1, 3, 12, 0, 0]
        result = moveZeroes(nums)
        self.assertListEqual(result, expected)

    def test_2(self):
        nums = [0]
        expected = [0]
        result = moveZeroes(nums)
        self.assertListEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

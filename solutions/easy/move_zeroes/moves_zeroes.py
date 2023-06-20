import unittest
from typing import List


def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    # Collect zero, move everything to the left in the array.
    # 1. Traverse backwards
    # 0, 1, 0, 3, 12
    #             P
    #          P
    #       P -> Found 0
    # -> Move the last.
    # -> Move processed elements to the left by one index.
    # 0, 1, 3, 12, 0
    #    P
    # P -> Found 0
    # -> Move the 0 to the last
    # -> Move processed elements to the left by one index.
    for num in nums:
        if num == 0:
            print(0)



class PlusOneTestCase(unittest.TestCase):
    def test_1(self):
        nums = [0, 1, 0, 3, 12]
        expected = [1, 3, 12, 0, 0]
        moveZeroes(nums)
        # self.assertListEqual(result, expected)

    def test_2(self):
        nums = [0]
        expected = [0]
        result = moveZeroes(nums)
        self.assertListEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

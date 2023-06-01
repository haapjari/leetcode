import unittest


class Solution:
    def rotate(self, nums, k):
        """
        Rotate the array to the right by k steps.
        """
        # Move in-place.

        # Create New Array
        # New Starting Point is len(nums) - k

        # First Shift Everything to Right by 1.
        # Then Store "Shift" to a Function in a Way it takes Arr as
        i = 0
        while i < len(nums):
            if i == 0:
                before_index = len(nums) - 1
            else:
                before_index = i - 1
            current_index = i
            if i == len(nums):
                current_index = 0
            after_index = current_index + 1
            if after_index == len(nums):
                after_index = 0

            # first calculate the indices of curr, after and before.
            # then assign values using temp
            # repeat in loop

            print(f"before: {before_index}")
            print(f"curr: {current_index}")
            print(f"after: {after_index}")

            i += 1

class TestSolution(unittest.TestCase):
    def test_rotate_case_1(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3

        s = Solution()
        s.rotate(nums, k)

        # assert that the result is correct
        # self.assertEqual(nums, [5, 6, 7, 1, 2, 3, 4])

    def test_rotate_case_2(self):
        nums = [-1, -100, 3, 99]
        k = 2

        s = Solution()
        s.rotate(nums, k)

        # assert that the result is correct
        self.assertEqual(nums, [3, 99, -1, -100])

    def test_rotate_case_3(self):
        nums = [1, 2, 3]
        k = 4

        s = Solution()
        s.rotate(nums, k)

        # assert that the result is correct
        self.assertEqual(nums, [3, 1, 2])


if __name__ == '__main__':
    unittest.main()
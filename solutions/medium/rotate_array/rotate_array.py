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
        counter = 0
        iterations = len(nums)
        curr = len(nums) - k
        while counter < iterations:
            before = curr - 1
            after = curr + 1
            if curr == len(nums):
                curr = 0

            # before and after roll to 7, solve this

            print(f"before index: {before}")
            print(f"current index: {curr}")
            print(f"after index: {after}")

            curr += 1
            counter += 1

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
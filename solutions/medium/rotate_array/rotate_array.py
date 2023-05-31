import unittest


class Solution:
    def rotate(self, nums, k):
        """
        Rotate the array to the right by k steps.
        """
        pass  # Your code goes here


class TestSolution(unittest.TestCase):
    def test_rotate_case_1(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3

        s = Solution()
        s.rotate(nums, k)

        # assert that the result is correct
        self.assertEqual(nums, [5, 6, 7, 1, 2, 3, 4])

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
import unittest


class Solution:
    def rotate(self, nums, k):
        """
        Rotate the array to the right by k steps.
        """
        x = k % len(nums)

        # Call a Slice Operation "::", and in reverse order "-1", end up reversing the list.
        # Don't assign new variable, instead refer to original variable with all elements,
        # end up not allocating more space, and modifying this in place.
        nums[:] = nums[::-1]

        # Access the elements until x and reverse them.
        nums[:x] = nums[:x][::-1]

        # Access the elements after x and reverse them.
        nums[x:] = nums[x:][::-1]


class TestSolution(unittest.TestCase):
    def test_rotate_case_1(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3

        s = Solution()
        s.rotate(nums, k)

        self.assertEqual(nums, [5, 6, 7, 1, 2, 3, 4])

    def test_rotate_case_2(self):
        nums = [-1, -100, 3, 99]
        k = 2

        s = Solution()
        s.rotate(nums, k)

        self.assertEqual(nums, [3, 99, -1, -100])

    def test_rotate_case_3(self):
        nums = [1, 2, 3]
        k = 4

        s = Solution()
        s.rotate(nums, k)

        self.assertEqual(nums, [3, 1, 2])


if __name__ == '__main__':
    unittest.main()
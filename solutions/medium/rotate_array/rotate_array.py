import unittest


class Solution:
    def rotate(self, nums, k):
        """
        Rotate the array to the right by k steps.
        """

        def reverse_list(list):
            start = 0
            end = len(list) - 1

            while start < end:
                list[start], list[end] = list[end], list[start]
                start += 1
                end -= 1

        # This gives the starting position. Modulo
        # makes sure, that the k is always in between
        # the correct length.
        x = k % len(nums)

        reverse_list(nums)

        tmp = nums[:x]
        tmp.reverse()

        print(tmp)

        tmp = nums[x:]
        tmp.reverse()

        print(tmp)

        #reverse_list(nums[:x])
        #reverse_list(nums[x:])

        #print(nums)

        # reverse the list
        # split to k
        # reverse the splitted parts

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
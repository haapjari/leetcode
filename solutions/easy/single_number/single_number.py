import unittest


def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Implement your solution here

    print()

    seen = None
    for i in range(len(nums)):
         
        




class SingleNumberTestCase(unittest.TestCase):
    def test_1(self):
        nums = [2, 2, 1]
        expected = 1
        result = singleNumber(nums)
        # self.assertEqual(result, expected)

#    def test_2(self):
#        nums = [4, 1, 2, 1, 2]
#        expected = 4
#        result = singleNumber(nums)
#        self.assertEqual(result, expected)
#
#    def test_3(self):
#        nums = [1]
#        expected = 1
#        result = singleNumber(nums)
#        self.assertEqual(result, expected)
#
#    def test_4(self):
#        nums = [5, 7, 5, 6, 6]
#        expected = 7
#        result = singleNumber(nums)
#        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

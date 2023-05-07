import  unittest
from src.two_sum.two_sum import twoSum

class TwoSumTestCase(unittest.TestCase):
    def test_1(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        result = twoSum(nums, target)
        self.assertEqual(result, expected)
    
    def test_2(self):
        nums = [3,2,4]
        target = 6 
        expected = [1, 2]
        result = twoSum(nums, target)
        self.assertEqual(result, expected)
    
    def test_3(self):
        nums = [3, 3]
        target = 6 
        expected = [0, 1]
        result = twoSum(nums, target)
        self.assertEqual(result, expected)

    def test_4(self):
        nums = [2, 5, 5, 11]
        target = 10
        expected = [1, 2]
        res = twoSum(nums, target)
        self.assertEqual(res, expected)
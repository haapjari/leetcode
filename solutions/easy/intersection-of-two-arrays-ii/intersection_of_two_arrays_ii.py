import unittest
from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    # return array which contains elements that appear in both arrays

    # check which list is smaller
    # only check the smaller values
    # create new array and return it

    intersection = []

    if len(nums1) < len(nums2):
        smaller_list = nums1
        larger_list = nums2
    else:
        smaller_list = nums2
        larger_list = nums1

    for i in range(len(smaller_list)):
        print(smaller_list[i])
        if smaller_list[i] in larger_list:
            # Return already processed values.
            larger_list.remove(smaller_list[i])
            intersection.append(smaller_list[i])

    return intersection

class IntersectTestCase(unittest.TestCase):
    def test_1(self):
        nums1 = [1, 2, 2, 1]
        nums2 = [2, 2]
        expected = [2, 2]
        result = intersect(nums1, nums2)
        self.assertCountEqual(result, expected)

    def test_2(self):
        nums1 = [4, 9, 5]
        nums2 = [9, 4, 9, 8, 4]
        expected = [4, 9]
        result = intersect(nums1, nums2)
        self.assertCountEqual(result, expected)

    def test_3(self):
        nums1 = [3,1,2]
        nums2 = [1,1]
        expected = [1]
        result = intersect(nums1, nums2)
        self.assertCountEqual(result, expected)

    # Add more tests here for edge cases if necessary


if __name__ == '__main__':
    unittest.main()

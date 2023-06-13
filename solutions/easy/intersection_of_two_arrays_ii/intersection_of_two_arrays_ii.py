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
    length = None
    smallerList = []
    biggerList = []
    retList = []
    if len(nums1) > len(nums2):
        length = len(nums2)
        smallerList = nums2
        biggerList = nums1
    else:
        length = len(nums1)
        smallerList = nums1
        biggerList = nums2

    i = 0
    while i < length:
        if smallerList[i] in biggerList:
            retList.append(smallerList[i])
        i += 1

    return retList

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

    # Add more tests here for edge cases if necessary


if __name__ == '__main__':
    unittest.main()

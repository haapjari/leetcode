import unittest

def removeDuplicates(nums: list) -> int:
    """
    :type nums: List[int]
    :rtype: int
    """

    seen = []

    for num in nums:
        if num not in seen:
            seen.append(num)

    i = 0
    while i < len(seen):
        nums[i] = seen[i]
        i += 1

    j = len(seen)
    while j < len(nums):
        nums[j] = "_"
        j += 1


    return len(seen)

class RemoveDuplicatesTestCase(unittest.TestCase):
    def test_1(self):
        nums = [1, 1, 2]
        expected = 2
        result = removeDuplicates(nums)
        self.assertEqual(result, expected)
        # self.assertListEqual(nums[:result], [1, 2])
        self.assertListEqual([1, 2], nums[:result])

    def test_2(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        expected = 5
        result = removeDuplicates(nums)
        self.assertEqual(result, expected)
        self.assertListEqual(nums[:result], [0, 1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()

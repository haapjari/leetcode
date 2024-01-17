import unittest


def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    # Implement your solution here

    seen = set()

    for i in nums:
        if i not in seen:
            seen.add(i)

    if len(seen) < len(nums):
        return True

    return False


class ContainsDuplicateTestCase(unittest.TestCase):
    def test_1(self):
        nums = [1, 2, 3, 1]
        expected = True
        result = containsDuplicate(nums)
        self.assertEqual(result, expected)

    def test_2(self):
        nums = [1, 2, 3, 4]
        expected = False
        result = containsDuplicate(nums)
        self.assertEqual(result, expected)

    def test_3(self):
        nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        expected = True
        result = containsDuplicate(nums)
        self.assertEqual(result, expected)

    # Add more tests here for edge cases if necessary


if __name__ == '__main__':
    unittest.main()

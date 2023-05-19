import unittest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Given a string s, find the length of the longest substring, without repeating characters.
        Edge Cases:
        """

        # What is a substring (?)
        # Substring a sequence of characters, without having duplicate characters.
        # There has to be check in place, which checks, if the character has been processed already.
        # Every possible substring has to be checked, to there has to be check for substring starting
        # from every point of the string. (Substring starting from index 0, if thats longer than
        # longest known substring, replace longest substring -> proceed to next index.)

        seen = []
        longest_substring_length = 0

        # this now goes through the all the substrings from index 0
        # this actual just returns the amount of unique characters in a string
        for char in s:
            if char in seen:
                continue

            print(char)

            seen.append(char)

        return len(seen)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        s = "abcabcbb"
        expected_output = 3
        actual_output = self.solution.lengthOfLongestSubstring(s)
    #     self.assertEqual(actual_output, expected_output, "Expected the length of longest substring to be 3")

    # def test_example2(self):
    #     s = "bbbbb"
    #     expected_output = 1
    #     actual_output = self.solution.lengthOfLongestSubstring(s)
    #     self.assertEqual(actual_output, expected_output, "Expected the length of longest substring to be 1")

    # def test_example3(self):
    #     s = "pwwkew"
    #     expected_output = 3
    #     actual_output = self.solution.lengthOfLongestSubstring(s)
    #     self.assertEqual(actual_output, expected_output, "Expected the length of longest substring to be 3")


if __name__ == "__main__":
    unittest.main()

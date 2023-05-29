import unittest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        i = 0
        # Loop through the origin String.
        while i < len(s):
            # Substring to analyze is the current index and rest of the
            # characters.
            substring = s[i:]

            # Loop through the substring, track the seen characters.
            seen = []
            for char in substring:
                # If character has been seen at least once,
                # stop analyzing the substring.
                if char in seen:
                   break
                else:
                    seen.append(char)

            # Compute the longest unique characters withing the substring.
            if longest < len(seen):
                longest = len(seen)

            i += 1

        # Return the longest unique characters withing the substring.
        return longest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        s = "abcabcbb"
        expected_output = 3
        actual_output = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(actual_output, expected_output, "Expected the length of longest substring to be 3")

    def test_example2(self):
         s = "bbbbb"
         expected_output = 1
         actual_output = self.solution.lengthOfLongestSubstring(s)
         self.assertEqual(actual_output, expected_output, "Expected the length of longest substring to be 1")

    def test_example3(self):
        s = "pwwkew"
        expected_output = 3
        actual_output = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(actual_output, expected_output, "Expected the length of longest substring to be 3")


if __name__ == "__main__":
    unittest.main()

import unittest
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Determine if a 9x9 Sudoku board is valid.
        """
        # Function to check if numbers are unique (excluding '.')
        def valid(nums):
            filtered_nums = []
            # Filter out the "." characters.
            for num in nums:
                if num != '.':
                    filtered_nums.append(num)
            nums = filtered_nums

            # Compare the lengths. Set doesn't allow anything, but unique numbers
            # this is why, the length of a set of nums, includes only the unique
            # numbers. If the lengths are different, that means that the filtered
            # nums includes non-unique numbers.
            return len(nums) == len(set(nums))

        # Check the Rows
        # for row in board:
        #     if not valid(row):
        #        return False

        # Check Columns
        #for i in range(9):
        #    for j in range(9):
        #        if not valid(board[j][i]):
        #            return False

        # STUDY THE SOLUTION
        # Check Sub-Grids
        # For every possible 3x3 square in the 9x9 board:

        # Loop through values of 0-9, with steps of 3, so we're taking indices 0, 3 and 6.
        for i in range(0, 9, 3):
            print(board[i])
            #for j in range(0, 9, 3):  # j takes on values: 0, 3, 6

                # Initialize an empty list to collect the values in the current 3x3 square.
                #square_values = []

                # Iterate over the rows of the current 3x3 square.
                #for x in range(i, i + 3):  # If i=0, x takes on values: 0, 1, 2
                    # If i=3, x takes on values: 3, 4, 5
                    # and so on...

                    # Iterate over the columns of the current 3x3 square.
                    #for y in range(j, j + 3):  # Analogous to the x loop

                        # Add the value at board[x][y] to our list.
                        #value = board[x][y]
                        #square_values.append(value)

                # After collecting all values in the 3x3 square, check if they're valid.
                #if not valid(square_values):
                #    return False

        return True

class TestSolution(unittest.TestCase):
    def test_isValidSudoku_case_1(self):
        s = Solution()
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]
        result = s.isValidSudoku(board)
        print(result)
        # self.assertTrue(s.isValidSudoku(board))

    def test_isValidSudoku_case_2(self):
        s = Solution()
        board = [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]
        self.assertFalse(s.isValidSudoku(board))

    def test_validate_rows_case_1(self):
        s = Solution()
        board = [
            ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."]
        ]
        self.assertTrue(s.validate_rows(board))

    def test_validate_columns_case_1(self):
        s = Solution()
        board = [
            ["1", ".", ".", ".", ".", ".", ".", ".", "."],
            ["2", ".", ".", ".", ".", ".", ".", ".", "."],
            ["3", ".", ".", ".", ".", ".", ".", ".", "."],
            ["4", ".", ".", ".", ".", ".", ".", ".", "."],
            ["5", ".", ".", ".", ".", ".", ".", ".", "."],
            ["6", ".", ".", ".", ".", ".", ".", ".", "."],
            ["7", ".", ".", ".", ".", ".", ".", ".", "."],
            ["8", ".", ".", ".", ".", ".", ".", ".", "."],
            ["9", ".", ".", ".", ".", ".", ".", ".", "."]
        ]
        self.assertTrue(s.validate_columns(board))

    def test_validate_subgrids_case_1(self):
        s = Solution()
        board = [
            ["1", "2", "3", ".", ".", ".", ".", ".", "."],
            ["4", "5", "6", ".", ".", ".", ".", ".", "."],
            ["7", "8", "9", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."]
        ]
        self.assertTrue(s.validate_subgrids(board))


if __name__ == '__main__':
    unittest.main()

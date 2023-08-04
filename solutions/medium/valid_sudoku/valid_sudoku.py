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
            # if not valid(row):
            #    return False

        # STUDY THE SOLUTION
        # Check Columns
        i = 0
        while i < len(board):
            print(board[i])

            i += 1


        #for i in range(9):
           #print(board[i])
           #for y in range[9]:
               #print(board[i][y])
           #if not is_valid([board[row][col] for row in range(9)]):
           # return False

        # STUDY THE SOLUTION
        # Check Sub-Grids
        #for i in range(0, 9, 3):
        #    for j in range(0, 9, 3):
        #        if not is_valid([board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]):
        #            return False

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

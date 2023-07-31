import unittest
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Determine if a 9x9 Sudoku board is valid.
        """

        # Loop the Board "Row" at a time. -> Validate
        # Loop the Board "Column" at a time. -> Validate
        # Loop the Board "Subgrid" at a time. -> Validate
        # If validations pass -> True

        return self.validate_rows(board)

    def validate_rows(self, board) -> bool:
        """
        Validates that each row of the board contains the digits 1-9 without repetition.
        """
        for row in board:
            seen = []
            for elem in row:
                if elem != ".":
                    seen.append(elem)
                if seen.count(elem) > 1:
                    return False

        return True

    def validate_columns(self, board) -> bool:
        """
        Validates that each column of the board contains the digits 1-9 without repetition.
        """
        pass  # Implementation here

    def validate_subgrids(self, board) -> bool:
        """
        Validates that each 3x3 subgrid of the board contains the digits 1-9 without repetition.
        """
        pass  # Implementation here


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

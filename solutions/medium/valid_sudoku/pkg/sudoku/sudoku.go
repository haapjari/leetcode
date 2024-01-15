package sudoku

import "fmt"

func IsValidSudoku(board [][]byte) bool {
	// TODO: Row
	// TODO: Column
	// TODO: 3x3 Box

	for _, row := range board {
		for _, cell := range row {
			fmt.Printf("%c ", cell)
		}
		fmt.Println()
	}

	return false
}

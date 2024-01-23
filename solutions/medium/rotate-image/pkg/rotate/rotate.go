package rotate

import "fmt"

func Rotate(matrix [][]int) [][]int {
	// Cursor to Top Left.
	// Copy value from Cursor to "temp".
	// Move Cursor to Top Right.
	// Swap value from Cursor to "temp".
	// Move Cursor to Bottom Right.
	// Swap value from Cursor to "temp".
	// Move Cursor to Bottom Left.
	// Swap value from Cursor to "temp".
	// Move Cursor to Top Left.
	// Swap value from Cursor to "temp".

	temp := matrix[0][0] // Temporarily store the top left corner.

	// Swap: Top Left with Top Right.
	topRightIndex := len(matrix[0]) - 1
	matrix[0][0] = matrix[0][topRightIndex]
	matrix[0][topRightIndex] = temp

	// Swap: Top Right with Bottom Right.
	bottomRightIndex := len(matrix) - 1
	temp = matrix[0][0]
	matrix[0][0] = matrix[bottomRightIndex][topRightIndex]
	matrix[bottomRightIndex][topRightIndex] = temp

	// Swap: Bottom Right, with Bottom Left.
	temp = matrix[0][0]
	matrix[0][0] = matrix[bottomRightIndex][0]
	matrix[bottomRightIndex][0] = temp

	// Print matrix to verify changes.
	for i := 0; i < len(matrix); i++ {
		for j := 0; j < len(matrix[i]); j++ {
			fmt.Printf("%v ", matrix[i][j])
		}
		fmt.Printf("\n")
	}

	// temp = topRightCorner
	// topRightCorner = cursor
	// cursor = temp

	// bottomRightCorner := matrix[len(matrix)-1][len(matrix[0])-1]

	// temp = bottomRightCorner
	// bottomRightCorner = cursor
	// cursor = temp

	// bottomLeftCorner := matrix[len(matrix)-1][0]

	// temp = topLeftCorner
	// bottomLeftCorner = cursor

	return nil
}

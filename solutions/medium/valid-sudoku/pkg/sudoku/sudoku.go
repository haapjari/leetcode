package sudoku

import (
	"log"
	"strconv"
)

func IsValidSudoku(board [][]byte) bool {
	if !validateRows(board) {
		return false
	}

	if !validateColumns(board) {
		return false
	}

	if !validateBoxes(board) {
		return false
	}

	return true
}

func validateRows(board [][]byte) bool {
	set := []int{}

	for _, row := range board {
		for _, char := range row {
			if string(char) != "." {
				i, err := strconv.Atoi(string(char))
				if err != nil {
					log.Fatalf("unable to convert char to int: %v", err)
				}

				set = append(set, i)
			}
		}

		// Check, whether all the numbers within set are unique.
		// After the set (numbers of a certain row) has been processed
		// reset the set.
		for i, num := range set {
			for j := 0; j < len(set); j++ {
				if i != j && num == set[j] {
					return false
				}
			}
		}

		// Empty the set.
		set = []int{}
	}

	return true
}

func validateColumns(board [][]byte) bool {
	set := []int{}

	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[i]); j++ {
			char := board[j][i]

			if string(char) != "." {
				i, err := strconv.Atoi(string(char))
				if err != nil {
					log.Fatalf("unable to convert char to int: %v", err)
				}

				set = append(set, i)
			}
		}

		// Check, whether all the numbers within set are unique.
		// After the set (numbers of a certain row) has been processed
		// reset the set.
		for i, num := range set {
			for j := 0; j < len(set); j++ {
				if i != j && num == set[j] {
					return false
				}
			}
		}

		// Empty the set.
		set = []int{}
	}

	return true
}

// TODO: All test cases are not passing, study this.
func validateBoxes(board [][]byte) bool {
	set := []int{}

	for row := 0; row < len(board); row++ {
		for col := 0; col < 3; col++ {
			char := board[row][col]
			if string(char) != "." {
				i, err := strconv.Atoi(string(char))
				if err != nil {
					log.Fatalf("unable to convert char to int: %v", err)
				}

				set = append(set, i)
			}
		}

		if (row+1)%3 == 0 && row != 0 {
			// Check, whether all the numbers within set are unique.
			// After the set (numbers of a certain row) has been processed
			// reset the set.
			for i, num := range set {
				for j := 0; j < len(set); j++ {
					if i != j && num == set[j] {
						return false
					}
				}
			}

			set = []int{}
		}
	}

	for row := 0; row < len(board); row++ {
		for col := 3; col < 6; col++ {
			char := board[row][col]
			if string(char) != "." {
				i, err := strconv.Atoi(string(char))
				if err != nil {
					log.Fatalf("unable to convert char to int: %v", err)
				}

				set = append(set, i)
			}
		}

		if (row+1)%3 == 0 && row != 0 {
			// Check, whether all the numbers within set are unique.
			// After the set (numbers of a certain row) has been processed
			// reset the set.
			for i, num := range set {
				for j := 0; j < len(set); j++ {
					if i != j && num == set[j] {
						return false
					}
				}
			}

			set = []int{}

		}
	}

	for row := 0; row < len(board); row++ {
		for col := 6; col < 9; col++ {
			char := board[row][col]
			if string(char) != "." {
				i, err := strconv.Atoi(string(char))
				if err != nil {
					log.Fatalf("unable to convert char to int: %v", err)
				}

				set = append(set, i)
			}
		}

		if (row+1)%3 == 0 && row != 0 {
			// Check, whether all the numbers within set are unique.
			// After the set (numbers of a certain row) has been processed
			// reset the set.
			for i, num := range set {
				for j := 0; j < len(set); j++ {
					if i != j && num == set[j] {
						return false
					}
				}
			}

			set = []int{}
		}
	}

	return true
}

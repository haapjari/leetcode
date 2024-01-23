package main

import (
	"fmt"
	"leetcode/pkg/rotate"
)

func main() {
	matrix := [][]int{
		{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9},
	}

	fmt.Println(rotate.Rotate(matrix))
}

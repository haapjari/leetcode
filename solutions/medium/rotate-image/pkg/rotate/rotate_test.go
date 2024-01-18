package rotate_test

import (
	"leetcode/pkg/rotate"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestRotate(t *testing.T) {
	t.Run("tbd", func(t *testing.T) {
		matrix := [][]int{
			{1, 2, 3},
			{4, 5, 6},
			{7, 8, 9},
		}

		expectedMatrix := [][]int{
			{7, 4, 1},
			{8, 5, 2},
			{9, 6, 3},
		}

		assert.Equal(t, expectedMatrix, rotate.Rotate(matrix))
	})
}

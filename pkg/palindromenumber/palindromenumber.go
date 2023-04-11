package palindronenumber

import (
	"reflect"
	"strconv"
)

// https://leetcode.com/problems/palindrome-number/
func IsPalindrome(x int) bool {
	str := strconv.Itoa(x)
	runeArray := []rune(str)
	reversedRuneArray := []rune{}

	for i := len(runeArray) - 1; i >= 0; i-- {
		reversedRuneArray = append(reversedRuneArray, runeArray[i])
	}

	return reflect.DeepEqual(runeArray, reversedRuneArray)
}

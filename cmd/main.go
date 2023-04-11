package main

import (
	"fmt"

	palindronenumber "github.com/haapjari/leetcode/pkg/palindromenumber"
)

func main() {
    fmt.Println(palindronenumber.IsPalindrome(121))
    fmt.Println(palindronenumber.IsPalindrome(1221))
    fmt.Println(palindronenumber.IsPalindrome(122221))
    fmt.Println(palindronenumber.IsPalindrome(123))
}

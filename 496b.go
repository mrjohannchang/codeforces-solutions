package main

import (
	"fmt"
)

func main() {
	var n int
	var init, res string

	fmt.Scan(&n)
	fmt.Scan(&init)

	for i := 0; i < n; i++ {
		res += "9"
	}

	for i := 0; i < n; i++ {
		var candidate string

		s := init[i:] + init[:i]
		diff := ('9' + 1 - s[0]) % 10

		for j := 0; j < n; j++ {
			candidate += string('0' + (s[j]+diff-'0')%10)
		}

		if candidate < res {
			res = candidate
		}
	}

	fmt.Println(res)
}

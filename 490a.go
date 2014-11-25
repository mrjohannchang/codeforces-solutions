package main

import (
	"fmt"
)

func main() {
	var n int

	fmt.Scan(&n)

	var t int
	var fields [3][]int

	for i := 0; i < 3; i++ {
		fields[i] = make([]int, 0)
	}

	for i := 1; i <= n; i++ {
		fmt.Scan(&t)
		t--
		fields[t] = append(fields[t], i)
	}

	min := len(fields[0])
	for i := 1; i < 3; i++ {
		if len(fields[i]) < min {
			min = len(fields[i])
		}
	}

	fmt.Println(min)

	for i := 0; i < min; i++ {
		fmt.Println(fields[0][i], fields[1][i], fields[2][i])
	}
}

package main

import (
	"fmt"
)

func max(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}

func main() {
	var a, b, c, d int

	fmt.Scan(&a, &b, &c, &d)

	m := max(3*a/10, a-a/250*c)
	v := max(3*b/10, b-b/250*d)

	var res string

	if m > v {
		res = "Misha"
	} else if m < v {
		res = "Vasya"
	} else {
		res = "Tie"
	}

	fmt.Println(res)
}

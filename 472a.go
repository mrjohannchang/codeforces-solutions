package main

import (
	"fmt"
)

func main() {
	var n int

	fmt.Scan(&n)

	x := n%2*5 + 4

	fmt.Println(x, n-x)
}

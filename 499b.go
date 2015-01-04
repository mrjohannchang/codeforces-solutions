package main

import (
	"fmt"
)

func main() {
	var n, m int
	var a, b string
	d := make(map[string]string)

	fmt.Scan(&n, &m)

	for i := 0; i < m; i++ {
		fmt.Scan(&a, &b)
		if len(a) > len(b) {
			d[a] = b
		} else {
			d[a] = a
		}
	}

	for i := 0; i < n; i++ {
		fmt.Scan(&a)
		fmt.Print(d[a])
		if i < n-1 {
			fmt.Print(" ")
		} else {
			fmt.Println()
		}
	}
}

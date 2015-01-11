package main

import (
	"fmt"
)

func main() {
	var n, p, q, r int

	fmt.Scan(&n)

	for i := 0; i < n; i++ {
		fmt.Scan(&p, &q)

		if q-p >= 2 {
			r++
		}
	}

	fmt.Println(r)
}

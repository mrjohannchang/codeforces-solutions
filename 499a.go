package main

import (
	"fmt"
)

func main() {
	var n, x, l, r, c, res int

	c = 1

	fmt.Scan(&n, &x)

	for i := 0; i < n; i++ {
		fmt.Scan(&l, &r)

		c = c + ((l-c)/x)*x
		res += r + 1 - c
		c = r + 1
	}

	fmt.Println(res)
}

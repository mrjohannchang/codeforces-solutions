package main

import (
	"fmt"
)

func main() {
	var n, max, min, res int
	min = 1000

	fmt.Scan(&n)

	a := make([]int, n)

	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])

		if i > 0 {
			if a[i]-a[i-1] > max {
				max = a[i] - a[i-1]
			}
		}

		if i > 1 {
			if a[i]-a[i-2] < min {
				min = a[i] - a[i-2]
			}
		}
	}

	res = min
	if max > min {
		res = max
	}

	fmt.Println(res)
}

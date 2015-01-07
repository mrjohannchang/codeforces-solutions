// Package main provides ...
package main

import (
	"fmt"
	"math"
	"sort"
)

func main() {
	var n, m, res int

	fmt.Scan(&n)

	a := make([]int, n)

	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}

	fmt.Scan(&m)

	b := make([]int, m)

	for i := 0; i < m; i++ {
		fmt.Scan(&b[i])
	}

	sort.Ints(a)
	sort.Ints(b)

	p := -1

	for i := 0; i < len(a); i++ {
		for j := p + 1; j < len(b); j++ {
			if math.Abs(float64(a[i])-float64(b[j])) <= 1 {
				p = j
				res++
				break
			}
		}
	}

	fmt.Println(res)
}

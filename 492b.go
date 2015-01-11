// Package main provides ...
package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

var reader = bufio.NewReader(os.Stdin)

func main() {
	var n, l int

	fmt.Fscan(reader, &n, &l)

	a := make([]int, n)

	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &a[i])
	}

	sort.Ints(a)

	var d float64

	for i := 0; i < n; i++ {
		if i == 0 {
			d = float64(a[i] - 0)
		}

		if i == n-1 {
			if float64(l-a[i]) > d {
				d = float64(l - a[i])
			}
		}

		if i == 0 {
			continue
		}

		if float64(a[i]-a[i-1])/2 > d {
			d = float64(a[i]-a[i-1]) / 2
		}
	}

	fmt.Println(d)
}

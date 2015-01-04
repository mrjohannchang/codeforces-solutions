package main

import (
	"fmt"
	"sort"
)

type pair struct {
	i, j int
}

func main() {
	var n, k int

	fmt.Scan(&n)

	a := make([]int, n)
	sortedA := make([]int, n)
	var swaps []pair

	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}

	copy(sortedA, a)
	sort.Ints(sortedA)

	for i := n - 1; i >= 0; i-- {
		if a[i] != sortedA[i] {
			var j int
			for j = 0; j < i; j++ {
				if a[j] == sortedA[i] {
					break
				}
			}
			p := pair{i: i, j: j}
			swaps = append(swaps, p)
			k++
			a[i], a[j] = a[j], a[i]
		}
	}

	fmt.Println(k)

	for i := 0; i < k; i++ {
		fmt.Println(swaps[i].i, swaps[i].j)
	}
}

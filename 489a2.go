package main

import (
	"fmt"
	"math"
)

type pair struct {
	i, j int
}

func minOfInts(a []int) (int, int) {
	value := math.MaxInt32
	var index int
	for i, v := range a {
		if v < value {
			index = i
			value = v
		}
	}
	return index, value
}

func main() {
	var n, k int

	fmt.Scan(&n)

	a := make([]int, n)
	var res []pair

	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}

	for i := 0; i < n; i++ {
		j, _ := minOfInts(a[i:])
		j += i
		if j != i {
			p := pair{i: i, j: j}
			res = append(res, p)
			k++
			a[i], a[j] = a[j], a[i]
		}
	}

	fmt.Println(k)

	for i := 0; i < k; i++ {
		fmt.Println(res[i].i, res[i].j)
	}
}

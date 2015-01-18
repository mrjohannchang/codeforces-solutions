package main

import (
	"fmt"
)

func main() {
	var n, m, res int
	fmt.Scan(&n, &m)
	table := make([][]byte, n)

	for i := 0; i < n; i++ {
		var row string
		fmt.Scan(&row)
		table[i] = []byte(row)
	}

	if n == 1 {
		fmt.Println(0)
		return
	}

	lcp := make([]int, n-1)

	for j := 0; j < len(table[0]); {
		illegal := false

		for i := 0; i < n-1; i++ {
			if lcp[i] < j {
				continue
			}

			if table[i][j] == table[i+1][j] {
				lcp[i]++
			} else if table[i][j] > table[i+1][j] {
				illegal = true
				break
			}
		}

		if !illegal {
			j++
		} else {
			res++

			for i := 0; i < n-1; i++ {
				if lcp[i] > j {
					lcp[i]--
				}
			}

			for i, l := 0, len(table[0]); i < n; i++ {
				if j < l-1 {
					table[i] = append(table[i][:j], table[i][j+1:]...)
				} else {
					table[i] = table[i][:j]
				}
			}
		}
	}

	fmt.Println(res)
}

package main

import (
	"fmt"
)

func main() {
	var n, q int
	d := make(map[string]string)

	fmt.Scan(&q)

	for i := 0; i < q; i++ {
		var oldH, newH string

		fmt.Scan(&oldH, &newH)

		origH, exists := d[oldH]

		if exists {
			d[newH] = origH
			delete(d, oldH)
		} else {
			d[newH] = oldH
			n++
		}
	}

	fmt.Println(n)

	for newH, oldH := range d {
		fmt.Println(oldH, newH)
	}
}

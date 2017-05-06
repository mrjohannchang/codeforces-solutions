// +build ignore

package main

import "fmt"

func main() {
	var l, r, ret int
	fmt.Scanf("%d %d", &l, &r)

	if l == r {
		ret = l
	} else {
		ret = 2
	}

	fmt.Println(ret)
}

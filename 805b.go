// +build ignore

package main

import "fmt"

func main() {
	var n int

	fmt.Scanf("%d", &n)

	name := make([]rune, n)

	for i := 0; i < n; i++ {
		switch i % 4 {
		case 0, 1:
			name[i] = 'a'
		case 2, 3:
			name[i] = 'b'
		}
	}

	fmt.Println(string(name))
}

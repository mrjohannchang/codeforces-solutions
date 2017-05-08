// +build ignore

package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

func main() {
	var s string
	buf := make([]byte, int(math.Pow(10, 7)))

	scanner := bufio.NewScanner(os.Stdin)
	scanner.Buffer(buf, int(math.Pow(10, 7)))

	if !scanner.Scan() {
		panic(scanner.Err())
	}

	fmt.Sscanf(scanner.Text(), "%s", &s)

	var a, ret uint64
	a = 1
	m := uint64(math.Pow(10, 9)) + 7

	for _, v := range s {
		if v == 'a' {
			a = a << 1 % m
			continue
		}

		ret = (ret + a - 1) % m
	}

	fmt.Println(ret)
}

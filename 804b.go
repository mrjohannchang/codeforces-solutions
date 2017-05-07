// +build ignore

package main

import (
	"bufio"
	"fmt"
	"math"
	"math/big"
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

	a, res, aMod := &big.Int{}, &big.Int{}, &big.Int{}
	m := big.NewInt(int64(math.Pow(10, 9)) + 7)
	one, two := big.NewInt(1), big.NewInt(2)

	for _, v := range s {
		if v == 'a' {
			a.Add(a, one)
			continue
		}

		aMod.Exp(two, a, m)
		res.Add(res, aMod)
		res.Add(res, m)
		res.Sub(res, one)
		res.Mod(res, m)
	}

	fmt.Println(res.Uint64())
}

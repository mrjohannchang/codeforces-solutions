package main

import (
	"fmt"
	"math/big"
)

func main() {
	var nString string
	n, res := big.NewInt(0), big.NewInt(0)

	fmt.Scan(&nString)
	n, _ = n.SetString(nString, 10)

	res.Div(n, big.NewInt(2))
	_, m := new(big.Int).DivMod(n, big.NewInt(2), big.NewInt(0))

	if m.Cmp(big.NewInt(0)) > 0 {
		res.Add(res, n.Neg(n))
	}

	fmt.Println(res)
}

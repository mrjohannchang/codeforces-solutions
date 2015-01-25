package main

import (
	"fmt"
	"math"
)

func main() {
	var r, x, y, xp, yp int64

	fmt.Scan(&r, &x, &y, &xp, &yp)

	fmt.Println((int64(math.Ceil(math.Sqrt(float64((xp-x)*(xp-x)+
		(yp-y)*(yp-y))))) + 2*r - 1) / (2 * r))
}

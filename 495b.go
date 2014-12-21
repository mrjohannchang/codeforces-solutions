package main

import (
	"fmt"
	"math"
)

func countDivisor(a, b int) int {
	q := a - b
	ret := 0
	sqrtQ := math.Sqrt(float64(q))
	for i := 1; float64(i) < sqrtQ; i++ {
		if q%i != 0 || q/i < b {
			continue
		}
		ret++
		if i <= b {
			continue
		}
		ret++
	}
	if sqrtQ > float64(b) && int(sqrtQ)*int(sqrtQ) == q {
		ret++
	}
	return ret
}

func main() {
	var a, b int
	fmt.Scanf("%d %d", &a, &b)

	if a < b || (a != b && a-b <= b) {
		fmt.Println(0)
	} else if a == b {
		fmt.Println("infinity")
	} else {
		fmt.Println(countDivisor(a, b))
	}
}

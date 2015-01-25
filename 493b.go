package main

import (
	"bufio"
	"fmt"
	"os"
)

var readWriter = bufio.NewReadWriter(
	bufio.NewReader(os.Stdin),
	bufio.NewWriter(os.Stdout))

func sum(a []int64) (b int64) {
	for i := 0; i < len(a); i++ {
		b += a[i]
	}
	return
}

func lexicographyCompare(a, b []int64) int {
	var n int

	if len(a) > len(b) {
		n = len(b)
	} else {
		n = len(a)
	}

	for i := 0; i < n; i++ {
		if a[i] > b[i] {
			return 1
		} else if a[i] < b[i] {
			return -1
		}
	}

	return 0
}

func main() {
	defer readWriter.Flush()

	var n int
	var a int64
	var xs, ys []int64
	var last string

	const FIRST, SECOND string = "first", "second"

	fmt.Fscan(readWriter, &n)

	for i := 0; i < n; i++ {
		fmt.Fscan(readWriter, &a)

		if a > 0 {
			xs = append(xs, a)
		} else {
			ys = append(ys, -a)
		}
	}

	if a > 0 {
		last = FIRST
	} else {
		last = SECOND
	}

	var sumOfXs, sumOfYs int64 = sum(xs), sum(ys)

	if sumOfXs > sumOfYs {
		fmt.Fprintln(readWriter, FIRST)
	} else if sumOfXs < sumOfYs {
		fmt.Fprintln(readWriter, SECOND)
	} else {
		result := lexicographyCompare(xs, ys)
		if result > 0 {
			fmt.Fprintln(readWriter, FIRST)
		} else if result < 0 {
			fmt.Fprintln(readWriter, SECOND)
		} else {
			fmt.Fprintln(readWriter, last)
		}
	}
}

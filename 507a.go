package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

type a struct {
	days, index int
}

type aSlice []a

func (as aSlice) Len() int {
	return len(as)
}

func (as aSlice) Less(i, j int) bool {
	if as[i].days < as[j].days {
		return true
	} else {
		return false
	}
}

func (as aSlice) Swap(i, j int) {
	as[i], as[j] = as[j], as[i]
}

var readWriter = bufio.NewReadWriter(
	bufio.NewReader(os.Stdin),
	bufio.NewWriter(os.Stdout))

func main() {
	defer readWriter.Flush()

	var n, k, m int

	fmt.Fscan(readWriter, &n, &k)

	as := make(aSlice, n)

	for i := 0; i < n; i++ {
		fmt.Fscan(readWriter, &(as[i].days))
		as[i].index = i + 1
	}

	sort.Sort(as)

	for _, a := range as {
		if k-a.days < 0 {
			break
		}

		k = k - a.days
		m++
	}

	fmt.Fprintln(readWriter, m)

	for i := 0; i < m; i++ {
		fmt.Fprint(readWriter, as[i].index)
		fmt.Fprint(readWriter, " ")
	}

	if m > 0 {
		fmt.Fprintln(readWriter)
	}
}

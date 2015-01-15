package main

import (
	"bufio"
	"fmt"
	"os"
)

var readWriter = bufio.NewReadWriter(bufio.NewReader(os.Stdin), bufio.NewWriter(os.Stdout))

func main() {
	defer readWriter.Flush()

	var n int

	fmt.Fscan(readWriter, &n)

	data := make([][2]int, n)
	var results [][2]int

	var queue []int

	for i := 0; i < n; i++ {
		fmt.Fscan(readWriter, &data[i][0], &data[i][1])

		if data[i][0] == 1 {
			queue = append(queue, i)
		}
	}

	for len(queue) > 0 {
		index := queue[0]

		if data[index][0] == 0 {
			queue = queue[1:len(queue)]
			continue
		}

		if data[index][0] == 1 {
			data[index][0]--
			data[data[index][1]][0]--
			data[data[index][1]][1] ^= index
			queue = append(queue, data[index][1])

			result := [2]int{index, data[index][1]}
			results = append(results, result)
		}

		queue = queue[1:len(queue)]
	}

	fmt.Fprintln(readWriter, len(results))

	for i := 0; i < len(results); i++ {
		fmt.Fprintln(readWriter, results[i][0], results[i][1])
	}
}

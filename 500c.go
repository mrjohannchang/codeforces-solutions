package main

import (
	"bufio"
	"container/list"
	"fmt"
	"os"
)

var reader = bufio.NewReader(os.Stdin)

func main() {
	var n, m int

	fmt.Fscan(reader, &n, &m)

	w := make([]int, n)
	b := make([]int, m)

	d := make([]int, n)
	rs := list.New()

	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &w[i])
	}

	for i := 0; i < m; i++ {
		var j int
		fmt.Fscan(reader, &j)
		b[i] = j - 1
	}

	for i := 0; i < m; i++ {
		if d[b[i]] == 0 {
			rs.PushBack(b[i])
		}
		d[b[i]] = 1
	}

	for i := 0; i < n; i++ {
		if d[i] == 0 {
			rs.PushBack(i)
		}
		d[i] = 1
	}

	var res int

	for i := 0; i < m; i++ {
		e := new(list.Element)
		for e = rs.Front(); e != nil; e = e.Next() {
			if e.Value == b[i] {
				break
			}
			j, _ := e.Value.(int)
			res += w[j]
		}
		rs.Remove(e)
		rs.PushFront(e.Value)
	}

	fmt.Println(res)
}

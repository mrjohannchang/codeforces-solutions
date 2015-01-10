package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	const YES = "YES"
	const NO = "NO"

	var publicKey string
	var a, b int

	reader := bufio.NewReader(os.Stdin)

	fmt.Fscan(reader, &publicKey)
	fmt.Fscan(reader, &a, &b)

	keyLength := len(publicKey)

	digits := make([]int, keyLength)
	modsOfA := make([]int, keyLength)
	modsOfB := make([]int, keyLength)

	modsOfA[0], _ = strconv.Atoi(string(publicKey[0]))
	modsOfB[keyLength-1], _ = strconv.Atoi(string(publicKey[keyLength-1]))

	modsOfA[0] = modsOfA[0] % a
	modsOfB[keyLength-1] = modsOfB[keyLength-1] % b

	res := NO
	var resInd int

	for i := 1; i < keyLength-1; i++ {
		d, _ := strconv.Atoi(string(publicKey[i]))
		digits[i] = d
		modsOfA[i] = (modsOfA[i-1]*10 + d) % a
	}

	for m, i := 1, keyLength-2; i >= 0; i-- {
		m = m * 10 % b
		modsOfB[i] = (digits[i]*m + modsOfB[i+1]) % b
		if modsOfA[i] == 0 && modsOfB[i+1] == 0 && publicKey[i+1] != '0' {
			res = YES
			resInd = i + 1
			break
		}
	}

	fmt.Println(res)

	if res == YES {
		fmt.Println(publicKey[:resInd])
		fmt.Println(publicKey[resInd:])
	}
}

package main

import (
	"fmt"
)

func main() {
	var home, away string
	var n int
	homePlayers := make([]int, 100)
	awayPlayers := make([]int, 100)

	fmt.Scan(&home, &away, &n)

	for i := 0; i < n; i++ {
		var t, no int
		var team, card string
		var players []int

		fmt.Scan(&t, &team, &no, &card)

		if team == "h" {
			players = homePlayers
			team = home
		} else {
			players = awayPlayers
			team = away
		}

		if players[no] >= 2 {
			continue
		}

		if card == "y" {
			players[no]++
		} else {
			players[no] += 2
		}

		if players[no] >= 2 {
			fmt.Println(team, no, t)
		}
	}
}

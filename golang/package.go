package main

import "fmt"

func main() {

	for i := 0; i <= 5; i++ {
	LABEL1:
		for j := 0; j <= 5; j++ {
			if j == 4 {
				continue LABEL1
			}
			fmt.Printf("i is: %d, and j is: %d\n", i, j)
		}
	}

}

package main

import (
	"fmt"
	"time"
)

// 10000
// 91.45266ms

// 100000
// 9.271935118s
func main() {
	count := 10000
	start := time.Now()
	// fmt.Println(start)
	var z float64 = 0
	for x := 0; x < count; x ++ {
		for y := 0; y < count; y ++ {
			z += 1
		}
	}
	end := time.Now()
	// fmt.Println(end)
	elapsed := end.Sub(start)
	fmt.Println(z)
	fmt.Println(elapsed)
}
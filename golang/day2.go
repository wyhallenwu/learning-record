package main

import (
	"fmt"
	"strings"
)

func main() {
	addPNG := FileAddSuffix(".png")
	file := "pic1"
	file = addPNG(file)
	fmt.Println(file)
}

func FileAddSuffix(suffix string) func(string) string {
	return func(name string) string {
		if !strings.HasSuffix(name, suffix) {
			return name + suffix
		}
		return name
	}
}

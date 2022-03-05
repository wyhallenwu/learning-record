package main

import (
	"fmt"
	"os"
	"runtime"
)

// 常量
const name string = "wuyuheng"
const pi float32 = 3.14159
const id = "1234" // 隐式推断类型
// const name, pi, id = "wuyuheng", 3.14159, "1234"

// const (
// 	name = "wuyuheng"
// 	pi   = 3.14159
// 	id   = "1234"
// )

func sayHello(name string) {
	fmt.Println("hello ", name)
}

func main() {
	aFunc := func(name string) string {
		return name + id
	}

	sayHello(aFunc(name))
	fmt.Printf("%T\n", aFunc(name))
	fmt.Println("hello world")

	var goos string = runtime.GOOS
	fmt.Println(goos)
	path := os.Getenv("PATH")
	fmt.Printf("%s\n", path)

}

package main

import "fmt"

var (
	name string
	age int
	height int
)

func main(){
	variables()
	helloName("Cassandra")
	helloName("Juliette")
	age = 21
	fmt.Println(sum(4,float32(age)))
	fmt.Println(convertAndSum(5, "5"))
	height = 2
	isMinimumHeight(float32(height))
	openFile("hello.txt")
	firstLoop()
	secondLoop()
}
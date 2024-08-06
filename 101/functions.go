package main

import (
	"fmt"
	"strconv"
)

func helloName(name string){
	fmt.Println("Hello", name)
}

func sum(n1, n2 float32) float32 {
	return n1 + n2;
}

func convertAndSum(a int, b string) (total int, err error) {
	i, err := strconv.Atoi(b)

	if err != nil{
		return
	}

	total = i + a

	return
}
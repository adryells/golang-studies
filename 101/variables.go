package main

import "fmt"


func variables(){
	message := "Pick me."
	name = "Adryell"

	var n1, n2, n3 float32;
	var n4 float32;
	n4++
	n1 = 8
	n2 = 9
	n3 = 7

	fmt.Println("Hello", name, ".", message)
	fmt.Println(n4, n3, n2, n1)

	n2, n3 = n3, n2
	fmt.Println(n2, n3)

}

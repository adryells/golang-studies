package main

import "fmt"

func slices(){
	// This is a slice
	names := []string{"Xerecovalda", "Cleitonres", "Xanilde", "Bundox"}
	fmt.Println(names, len(names), cap(names))

	names = append(names, "Chibaterson")
	fmt.Println(names, len(names), cap(names))
}
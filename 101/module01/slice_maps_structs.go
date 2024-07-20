package main

import "fmt"

func slices(){
	// This is a slice
	names := []string{"Xerecovalda", "Cleitonres", "Xanilde", "Bundox"}
	fmt.Println(names, len(names), cap(names))

	names = append(names, "Chibaterson")
	fmt.Println(names, len(names), cap(names))

	// Cria um slice do tipo int com 0 de tamanho e 10 de capacidade
	ages := make([]int, 0, 10)
	ages = append(ages, 1)
	fmt.Println(ages)
}

func maps(){
	weights := make(map[string]float32)
	weights["Adryell"] = 105
	weights["Jabulani"] = 200

	fmt.Println(weights)
	fmt.Println(weights["Jaw"])
	fmt.Println(weights["Adryell"])

	val, ok := weights["Danadinha"]
	fmt.Println(val, ok)

	val, ok = weights["Jabulani"]
	fmt.Println(val, ok)
}

func structs(){
	type Pessoa struct{
		Name string;
		Age uint8;
	}

	p := Pessoa{
		Name: "Adryell",
		Age: 21,
	}

	fmt.Println(p)
	fmt.Println(p.Name)
}
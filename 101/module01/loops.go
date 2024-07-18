package main

import "fmt"

func firstLoop(){
	for i:=0;i<10;i++{
		fmt.Println(i)
	}
}

func secondLoop(){
	names := []string{"Bucetovaldo", "Penilda", "Vaginete", "Bundoide", "Peiton"}
	for _, name := range names{
		fmt.Println(name);
	}
}

package main

import (
	"fmt"
	"log"
	"os"
)

func isMinimumHeight(height float32){
	if height < 1.75{
		fmt.Println("Lower")
	} else if height == 1.75{
		fmt.Println("Is equals")
	} else {
		fmt.Println("Greather")
	}
}

func openFile(fileName string) {
	file, err := os.Open(fileName)

	if err != nil{
		log.Panic(err)
	}

	data := make([]byte, 100)

	if _, err := file.Read(data); err != nil{
		log.Panic(err)
	}

	fmt.Println(string(data))
}

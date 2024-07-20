package main

import (
	"fmt"
	"time"
)

func goroutine_numeros(){
	for l := 'a'; l < 'j'; l++{
		fmt.Printf("%c", l);
		time.Sleep(time.Millisecond * 150)
	}
}

func goroutine_letras(){
	for n := 1; n < 10; n++{
		fmt.Println(n);
		time.Sleep(time.Millisecond * 250)
	}
}

func goroutines(){
	go goroutine_letras()
	go goroutine_numeros()
	time.Sleep(5 * time.Second) // Pro código nao morrer antes da execução das goroutines
}
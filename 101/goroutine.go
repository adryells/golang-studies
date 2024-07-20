package main

import (
	"fmt"
	"time"
)

// Channel só escreve
func goroutine_numeros(done chan <- bool){
	for l := 'a'; l < 'j'; l++{
		fmt.Printf("%c", l);
		time.Sleep(time.Millisecond * 150)
	}

	done <- true
}

// Channel só escreve
func goroutine_letras(done chan <- bool){
	for n := 1; n < 10; n++{
		fmt.Println(n);
		time.Sleep(time.Millisecond * 250)
	}

	done <- true
}

func goroutines(){
	channel_numeros := make(chan bool)
	channel_letras := make(chan bool)

	go goroutine_letras(channel_letras)
	go goroutine_numeros(channel_numeros)

	<- channel_letras
	<- channel_numeros

	 //time.Sleep(5 * time.Second) // Pro código nao morrer antes da execução das goroutines // A abordagem funciona mas é melhor usar channels

}
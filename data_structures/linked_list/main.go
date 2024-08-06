package main

import "fmt"

type Node struct {
	data int
	next *Node
}

type LinkedList struct {
	head *Node
}

// Add adiciona um novo nó ao final da lista
func (l *LinkedList) Add(data int) {
	newNode := &Node{data: data}
	if l.head == nil {
		l.head = newNode
	} else {
		current := l.head
		// Enquanto current.next tiver um next o for ocorre, quando not nil o for para.
		for current.next != nil {
			current = current.next
		}

		// Outra abordagem seria ter um Tail na LinkedList, aí não precisaria dessas iterações acima
		// O next do encontrado vira o novo Node
		current.next = newNode
	}
}

func (l *LinkedList) Remove(data int) {
	// Se a lista não tem head então tá vazia
	if l.head == nil {
		return
	}

	// Se o único elemento da lista for o data já mata aqui
	if l.head.data == data {
		l.head = l.head.next
		return
	}

	// Enquanto current.next não for nil e c.next não for oq tamo buscando vai atualizando o "current"
	current := l.head
	for current.next != nil && current.next.data != data {
		current = current.next
	}

	// Quando a condição do loop de cima for falsa, o next do current será o cara a ser deletado, então o novo next do current deve ser c.next.next
	if current.next != nil {
		current.next = current.next.next
	}
}

func (l *LinkedList) Print() {
	current := l.head
	for current != nil {
		fmt.Print(current.data, " -> ")
		current = current.next
	}
	fmt.Println("nil")
}

func main() {
	list := LinkedList{}

	list.Add(10)
	list.Add(20)
	list.Add(30)
	list.Print()

	list.Remove(20)
	list.Print()

	list.Remove(10)
	list.Print()
}

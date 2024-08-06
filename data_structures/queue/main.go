package main

import "fmt"

type Queue struct {
	Head *Node
	Tail *Node
}

type Node struct {
	Val  string
	Next *Node
}

func (q *Queue) Enqueue(name string) {
	node := Node{Val: name}

	if q.Head == nil {
		q.Head = &node
		q.Tail = &node
	} else {
		q.Tail.Next = &node
		q.Tail = &node
	}
}

func (q *Queue) Dequeue() string {
	if q.Head == nil {
		return ""
	}

	node := q.Head
	q.Head = q.Head.Next

	if q.Head == nil {
		q.Tail = nil
	}

	return node.Val
}

func main(){
	queue := Queue{}
	queue.Enqueue("Adryell")
	queue.Enqueue("Adryel")
	queue.Enqueue("Adrye")

	fmt.Println(queue.Dequeue())
	fmt.Println(queue.Dequeue())
	fmt.Println(queue.Dequeue())
}
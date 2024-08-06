package main

import "fmt"

type Stack struct{
	Tail *Node
	Count int
	Size int
}

type Node struct{
	Value string
	Next *Node
}

func (s *Stack) Push(value string){
	if s.Count == s.Size{
		panic("Stack Overflow")
	}

	node := Node{Value: value}

	if s.Tail != nil{
		node.Next = s.Tail
	}

	s.Tail = &node
	s.Count++
}

func (s *Stack) Pop() string{
	if s.Tail == nil{
		return ""
	}

	node := s.Tail
	s.Tail = node.Next

	s.Count--
	return node.Value
}

func main(){
	stack := Stack{Size:3}

	stack.Push("Adryell")
	stack.Push("Someone")
	stack.Push("Unknown")

	fmt.Println(stack.Pop())
	fmt.Println(stack.Pop())
	fmt.Println(stack.Pop())
}
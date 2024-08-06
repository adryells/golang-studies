package main

import (
	"fmt"
)

type HashTable struct {
	size  int
	table map[int][]*entry
}

type entry struct {
	key   string
	value string
}

func hash(key string, size int) int {
	// Para cada caractere da chave passa soma-se o valor ascii no hash inicializado em 0 e depois retorna o modulo do valor total pelo size
	hash := 0
	for _, char := range key {
		hash += int(char)
	}
	return hash % size
}

func NewHashTable(size int) *HashTable {
	return &HashTable{
		size:  size,
		table: make(map[int][]*entry, size),
	}
}

func (ht *HashTable) Insert(key, value string) {
	// Pega o tamanho da HshTable e passa como size do hash e também a key
	index := hash(key, ht.size)

	// O resultado do hash será o indice do elemento na tabela
	ht.table[index] = append(ht.table[index], &entry{key, value})
}

func (ht *HashTable) Search(key string) (string, bool) {
	index := hash(key, ht.size)
	for _, e := range ht.table[index] {
		if e.key == key {
			return e.value, true
		}
	}
	return "", false
}

func (ht *HashTable) Delete(key string) {
	index := hash(key, ht.size)
	for i, e := range ht.table[index] {
		if e.key == key {
			ht.table[index] = append(ht.table[index][:i], ht.table[index][i+1:]...)
			return
		}
	}
}

func main(){
	ht := NewHashTable(10)

	ht.Insert("name", "Adryell")
	ht.Insert("age", "21")
	ht.Insert("city", "Caxias")

	value, found := ht.Search("name")
	if found {
		fmt.Println("Found:", value)
	} else {
		fmt.Println("Not found")
	}

	value, found = ht.Search("country")
	if found {
		fmt.Println("Found:", value)
	} else {
		fmt.Println("Not found")
	}

	ht.Delete("city")

	value, found = ht.Search("city")
	if found {
		fmt.Println("Found:", value)
	} else {
		fmt.Println("Not found")
	}
}

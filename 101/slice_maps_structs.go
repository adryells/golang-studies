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

type Person struct{
	Name string;
	Age uint8;
	cpf string; // Privado pois inicial minuscula
}

// Para referenciar uma struct dentro dela deve se usar ponteiro (*)
type Category struct{
	Name string
	Parent *Category 
}

// Esse (c Category) serve para atrelar o metodo a uma struct, o "c" é uma convenção, no caso a primeira letra da struct
func (c Category) HasParent() bool{
	return c.Parent != nil;
}

// IMPORTANTE! Para alterar o valor de uma struct deve passa-la como ponteiro, senão ela irá como valor apenas legivel e não alteravel.
func (c *Category) setParent(parent *Category){
	c.Parent = parent;
}

// Equivalente ao __repr__ do Python
func (p Person) String() string{
	return fmt.Sprintf("Hello my name is %s and i am %dy.", p.Name, p.Age)
}
func structs(){
	p := Person{
		Name: "Adryell",
		Age: 21,
		cpf: "000.000.000-00",
	}

	fmt.Println(p)
	fmt.Println(p.Name)

	c := Category{
		Name: "A",
	}
	if !c.HasParent(){
		fmt.Println("Does not have a parent.")
	}

	c1 := Category{
		Name: "B",
		Parent: &c,
	}

	if c1.HasParent(){
		fmt.Println("Has parent.")
		fmt.Println(c1.Parent.Name)
	}

	c1.setParent(&Category{Name: "Veiudo"})
	fmt.Println(c1.Parent.Name)
}
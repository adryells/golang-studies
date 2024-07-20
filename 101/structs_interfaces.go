package main

import "fmt"

type Pessoa struct{
	Name string
	Age uint8 
}

type PessoaFisica struct{
	Pessoa
	Sobrenome string
	cpf string
}

type PessoaJuridica struct{
	Pessoa
	RazaoSocial string
	cnpj string
}


// Para uma struct implementar uma interface, a struct deve ter TODOS os metodos definidos pela interface atrelado a ela.
type Endurecer interface{
	Endurece() float32
}

func (pf PessoaFisica) Endurece() float32{
	return float32(pf.Age) * 1.6
}

func (pj PessoaJuridica) Endurece() float32{
	return float32(pj.Age) * 1.2
}

func show(e Endurecer){
	switch e.(type){
		case PessoaFisica: fmt.Println(e.(PessoaFisica).Sobrenome)
		case PessoaJuridica: fmt.Println(e.(PessoaJuridica).RazaoSocial)
		default: fmt.Println("Unknown")
	}

	// Checo se e é PessoaFisica. Se ok vier True, entra nas chaves. INTERFACE ASSERTION.
	// if e, ok := e.(PessoaFisica); ok{
	// 	fmt.Println(e.Sobrenome)
	// } 
}

func moreStructs(){
	p := Pessoa{
		Name: "Adryell",
		Age: 21,
	}

	pf := PessoaFisica{
		Pessoa: p,
		Sobrenome: "AC",
		cpf: "000.000.000-00",
	}

	pj := PessoaJuridica{
		Pessoa: p,
		RazaoSocial: "LTDA",
		cnpj: "00.000.000/0000-00",
	}

	fmt.Println(pf.Name)
	fmt.Println(pf)
	fmt.Println(pj.Endurece())
	fmt.Println(pf.Endurece())
	show(pf)
	show(pj)
}
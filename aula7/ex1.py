produto= ["Arroz", "Feijão","Macarrão","Carne bovina","Frango","Leite","Ovos",
    "Pão","Banana","Maçã","Tomate","Alface","Cebola","Batata","Cenoura","Óleo de cozinha",
    "Café","Açúcar","Sal","Detergente"]

print(produto[9]) #apenas um valor
print(produto[4:9]) #quando quiser mais de um valor

#append -para adicionar mais um na lista, apenas um argumento, no final
produto.append("Biscoito") 
print(produto)

#incert - é colocar em um lugar 
produto.insert(0,"Amendoim")
print(produto)
produto.insert(0,"Arroz")

#remove - para remover da lista pela str
produto.remove("Sal")
print(produto)

#pop - remove pelo indice (valor)
produto.pop(1)
print(produto)

#del - apagar da lista, mas n volta, pode ser fatiado tbm [0:4]
del produto[0]
print(produto)

#clear - exclui todos os valores da lista
produto.clear()
print(produto)

#sort - ordena de maneira crescente a-z ou 1 para 100
produto.sort()
print(produto)

#reverse - mostrar a lista invertida
#produto.sort(reverse=True)
produto.reverse()
print(produto)

#count - quantas vezes  um elemento existe dentro da lista
print(produto.count("Arroz"))

#index - qual posição tal elemento ta
print(produto.index("Cebola"))

#len () - descobrindo a quantidade de elementos existentes dentro da lista
print(len(produto))

#

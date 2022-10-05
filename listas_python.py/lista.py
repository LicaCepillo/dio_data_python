#Declaração de listas

frutas =["Laranja","Maçã","Uva"]
print(frutas)

frutas = []
print(frutas)

letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 4200000, 2020, "São Paulo", True]
print(carro)

#fatiamento de listas

frutas = ["maçã", "laranja","uva", "pera"]
print(frutas [0] ) #maçã
print(frutas [2] ) #uva

#indices negativos
frutas = ["maçã", "laranja","uva", "pera"]
print(frutas [-1] ) #pera
print(frutas [-2] ) #uva

#armazenar objetos em listas [],append
lista = []
lista.append(1)
lista.append("Python")
lista.append([40,30,20])
print(lista)

# Limpar a lista
lista = (1, "Python", [40,30,20])
##print(lista)
lista.clear()
print(lista)

#Retorna uma lista igual com isntancia diferente [].copyright()
lista1 = (1, "Python", [40,30,50])
l2= lista1.copy()
print(lista1)


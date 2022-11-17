pessoa = {"nome": "Guilherme", "idade": 28}
print (pessoa)

pessoa = dict( nome = "Guilherme", idade = 28)
print (pessoa)
#O dicionário aceita novas entradas, entretando se houver algum valor dentro de uma chave já existente, este valor será sobrescrito

#Adicionando telfone para o dicionário
pessoa ["telefone"] = "3333-1234"
print(pessoa)

#sobreescrevendo nome
pessoa["nome"] = "Maria"
print(pessoa)
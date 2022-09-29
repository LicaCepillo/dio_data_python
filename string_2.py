nome = "Lilian"
idade = 48
profissao = "Data Analyst"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Lilian", "idade": 42, "saldo": 45.435}

print("Nome: %s Idade: %s" % (nome, idade))

print("Nome: {} Idade: {}".format(nome,idade))

print("Nome: {1} Idade: {0}".format (idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age}".format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))

##f-string

print(f"None: {nome} Idade {idade}")
print(f"None: {nome} Idade {idade} Saldo: {saldo:10.2f}")

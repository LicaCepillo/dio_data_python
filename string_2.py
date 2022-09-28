nome = "Lilian"
idade = 48
profissao = "Data Analyst"
linguagem = "Python"

print("Nome: %s Idade: %s" % (nome, idade))
print("Nome: {} Idade: {}".format(nome,idade))
print("Nome: {1} Idade: {0}".format (idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age}".format(age=idade, name=nome))

contatos = {
    "lilian@gmail.com": {"nome": "Lilian", "telefone": "928035-246"}
}

#o dicionário original permanece igual, só a cópia que sofre alteração
copia = contatos.copy()
copia["lilian@gmail.com"] = {"nome": "Lica"}

print(copia)

#Adiconar novas chaves em um dicionário, existente ou não
dict.fromkeys(["nome","telefone"])

dict.fromkeys(["sexo","idade"], "vazio")
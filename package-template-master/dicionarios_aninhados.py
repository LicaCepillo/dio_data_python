contatos = {
    "guilherem@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3434-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "lilian@gmail.com": {"nome": "Lilian", "telefone": "333-6587","extra": {"a":"1"}},
}

telefone = contatos ["giovanna@gmail.com"]["telefone"]
print(telefone)

extra = contatos ["lilian@gmail.com"]["extra"]["a"]
print (extra) 

for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items ():
    print(chave, valor)
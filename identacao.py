def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado!")
        print("retire o seu dinheiro na boca do caixa")

    print("obrigada por ser noss cliente, tenha um dia!")

def depositar(valor):
    saldo = 500
    saldo += valor

sacar(100)
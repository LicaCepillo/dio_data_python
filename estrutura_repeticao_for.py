#texto = input("Informe um texto:")
texto = ""
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper()in VOGAIS:
        print(letra, end="")
else:        
    print() #adicionar uma quebra de linha
    print("Executa no final do laço")
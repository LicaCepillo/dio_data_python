texto = input("Informe um texto:")
VOGAIS = "AEIOU"

# exemplo utilizando um iterável valor letra in texto:
for letra in texto:
    if letra.upper()in VOGAIS:
        print(letra, end="")
else:        
    print() #adicionar uma quebra de linha
    

#exemplo utilizando a função build-in range

for numero in range (0,51, 5):
    print(numero, end=" ")


distancia_towers = int(input("Digite a distância entre as torres ( de 0 a 10000) :"))
diametro_saruman_tower = int(input("Digite o diametro da torre de Saruman (de 0 a 100) : "))
diametro_sauron_tower = int(input("Digite o diametro da torre de Sauron (de 0 a 100) : "))
diametros_towers = diametro_saruman_tower + diametro_sauron_tower
imc = str(distancia_towers/diametros_towers)

print(imc)

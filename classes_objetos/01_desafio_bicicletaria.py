class Bicicleta:
    def __imit__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = Valor

    def buzinar(self):
        print("Plim, plim...")
    
    def parar(self):  
        print("Parando bicicleta ...") 
        print("Bicicleta parada")

    def  correr(self):
        print("Vrummmmmm...")


b1 = Bicicleta("vermelha", "caloi", 2022, 600)

b1.buzinar()
b1.correr()
b1.parar()

print(b1.cor, b1.modelo, b1.ano, b1.valor)
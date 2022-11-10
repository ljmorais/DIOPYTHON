# Crie um modelo de registro para uma loja de bicicletas, onde informe: COR, MODELO, ANO E VALOR das bicicletas vendidas.Uma bicicleta pode ter BUZINA, CORRER, E PARAR. Adicione esses comportamentos.

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim Plim.....")

    def parar(self):
        print("Parando a bicicleta")
        print("Bicicleta parada.")
    
    def correr(self):
        print("Vruuum....")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta("vermelha", "Caloi", 2022, 600)

b1.buzinar()
b1.correr()
b1.parar()

print(b1)
""" 
Não lembro qual era essa atividade, então irei mante-la como desafio
"""

class Carro:
    def __init__(self, marca, modelo, ano, cor, velocidade=0):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = velocidade

    def acelerar(self, quantidade):
        self.velocidade += quantidade

    def frear(self, quantidade):
        if self.velocidade - quantidade < 0:
            self.velocidade = 0
        else:
            self.velocidade -= quantidade

    def ligar(self):
        print(f"{self.marca} {self.modelo} está ligado.")

    def desligar(self):
        print(f"{self.marca} {self.modelo} está desligado.")

    def status(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Cor: {self.cor}")
        print(f"Velocidade: {self.velocidade} km/h")

# Exemplo de uso da classe Carro
meu_carro = Carro("Toyota", "Corolla", 2022, "Prata")
meu_carro.ligar()
meu_carro.acelerar(60)
meu_carro.status()
meu_carro.frear(20)
meu_carro.status()
meu_carro.desligar()
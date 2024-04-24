# Desenvolva um exemplo de aplicação de polimorfismo utilizando super classe.
# Crie uma classe pai que defina um método genérico, e em seguida crie duas ou mais classes filhas que herdem essa super classe
# e sobrescrevam o método de acordo com suas necessidades.

class Animal:
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "O cachorro faz um som de latido."

class Gato(Animal):
    def emitir_som(self):
        return "O gato faz um som de miado."

def fazer_som(animal):
    return animal.emitir_som()

animal1 = Cachorro()
animal2 = Gato()

print(fazer_som(animal1))
print(fazer_som(animal2))
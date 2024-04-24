# Escreva um programa em Python que receba duas listas como entrada do usuário e retorne uma tupla contendo os elementos em comum entre as duas listas e a soma desses elementos.

def elementos_e_soma(lista_1, lista_2):
    elementosComum = []
    soma_elementos = 0

    for elemento in lista_1:
        if elemento in lista_2:
            elementosComum.append(elemento)
            soma_elementos += elemento

    return elementosComum, soma_elementos

lista_1 = [int(i) for i in input("Lista 1: ").split()]
lista_2 = [int(i) for i in input("Lista 2: ").split()]

resultado = elementos_e_soma(lista_1, lista_2)

print("Elementos em comum:", resultado[0])
print("Soma dos elementos em comum:", resultado[1])
# Escreva uma função em Python que recebe uma lista de números inteiros e retorna a média aritmética dos valores.

def calc_media(lista):
    if len(lista) == 0:
        return 0

    soma_num = sum(lista)
    media_num = soma_num / len(lista)
    return media_num

lista_numeros = [28, 29, 33, 58, 60]
media_num = calc_media(lista_numeros)

print('A média dos números é:', media_num)
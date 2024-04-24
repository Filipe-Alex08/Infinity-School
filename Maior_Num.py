#Escreva uma função em Python que recebe dois números como argumentos e retorna o maior entre eles.
# a) Implemente a função com o nome "maior_numero" e utilizando condicionais.
# b) Implemente a mesma função, porém utilizando a função "max".

#a)Exemplo 01:
def maior_num(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

resultado = maior_num(357, 468)
print(resultado)  

#b)Exemplo 02:
def maior_num(n1, n2):
    return max(n1, n2)

resultado = maior_num(357, 468)
print(resultado)
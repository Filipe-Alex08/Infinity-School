# Considere o seguinte trecho de código em Python:
# import random
# lista = [1, 2, 3, 4, 5]
# x = random.choice(lista)

# a)Explique o que o código faz.
# b)Escreva um trecho de código que use a função random para gerar um número inteiro aleatório entre 10 e 20 (inclusive).
# c)Escreva um trecho de código que use a função random para gerar uma lista com 5 elementos inteiros aleatórios entre 1 e 100 (inclusive).


# __________________________________________________________________________________________
# Resposta A:
"""O código importa o módulo radom, depois cria uma lista com números de 1 a 5. 
Na linha x = random.choice(lista) escolhe aleatoriamente um número da lista
e atribui o valor a variável x.
Então assim o código gera um número aleatório entre 1 a 5 e armazena-o em x."""

# Resposta B:
import random

num_aleatorio = random.randint(10,20)
print(num_aleatorio)

#Resposta C:
aleatoria_lista = [random.randint(1, 100) for _ in range(5)]
print(aleatoria_lista)

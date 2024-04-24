# Faça um programa em Python que, utilizando estruturas de repetição, calcule a média de idade dos alunos de uma turma.
# O programa deve pedir ao usuário a quantidade de alunos na turma e, em seguida, solicitar a idade de cada um. 
# O programa deve utilizar um laço FOR para receber as idades dos alunos e um laço WHILE para realizar a soma das idades. 
# Ao final, o programa deve exibir a média de idade da turma.

alunos = int(input('Digite a quantidade de alunos:'))

num_dividir = alunos
soma_idade = 0

while alunos > 0:
    for i in range(alunos):
        idade = int(input('Digite as idades dos alunos:'))
        break

    soma_idade = idade + soma_idade   
    alunos = alunos - 1  

media = soma_idade / num_dividir

print(f'A media das idades dos alunos é {media}')
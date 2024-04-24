"""
Crie um programa em Python que permita adicionar, remover e visualizar alunos e seus números de matrícula usando um dicionário.
O programa deve fornecer as seguintes funcionalidades:
Adicionar um aluno: O usuário poderá adicionar o nome e o número de matrícula de um aluno ao dicionário.
Remover um aluno: O usuário poderá remover um aluno do dicionário informando o número de matrícula.
Visualizar todos os alunos: O usuário poderá visualizar todos os alunos registrados no dicionário, exibindo seus respectivos números de matrícula.
O programa deve ser executado em um loop contínuo até que o usuário escolha sair.
"""

# Dicionario e Sets

alunos = {}

def adicionar_aluno():
    nome = input("Diga o nome do aluno: ") 
    matricula = input("Diga o n/ da matricula: ")
    alunos[matricula] = nome
    print("Aluno adicionado com Sucesso!! ")

def remover_aluno():
    matricula = input("Diga o n/ da matricula: ")
    if matricula in alunos:
        del alunos[matricula]
        print("Aluno removido/ Sucesso!! ")
    else:
        print("Matricula não econtrada!! ")

def visualizar_alunos():
    print("Lista de alunos: ")
    for matricula, nome in alunos.items():
        print(f"Matricula: {matricula}, Nome: {nome}")

# Loop contínuo
while True:
    print("\n Escolha uma opção:")
    print("1 - Adicionar aluno")
    print("2 - Remover aluno")
    print("3 - Visualizar alunos")
    print("4 - Sair")

    opcao = input("Opção:")
    if opcao == "1":
        adicionar_aluno()
    elif opcao == "2":
        remover_aluno()
    elif opcao == "3":
        visualizar_alunos()
    elif opcao == "4":
        break
    else:
        print("Opção invalida!")

print("Encerrando o programa...")
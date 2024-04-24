"""
Você foi contratado(a) para desenvolver um programa que gerencie um dicionário de alunos onde a chave deste dicionário é o número de matrícula dos próprios alunos. O programa deve permitir adicionar, remover, atualizar e listar os alunos.
Para isso, você deve implementar um módulo que contém as seguintes funções:
AdicionarAluno(): Solicita ao usuário que digite o nome e o número de matrícula de um aluno e adicione-o ao dicionário de alunos.
RemoverAluno(): Solicita ao usuário que digite o número de matrícula de um aluno e remove-o do dicionário de alunos.
AtualizarAluno(): Solicita ao usuário que digite o número de matrícula de um aluno e atualize o nome desse aluno no dicionário .
VerAlunos(): Lista todos os alunos cadastrados, exibindo o número de matrícula e o nome de cada um.

Lembre Se de Modularizar o código
"""

# Modulos e Bibliotecas

alunos = {}

def adicionar_aluno():
    matricula = input("Digite o número de matrícula do aluno: ")
    nome = input("Digite o nome do aluno: ")
    alunos[matricula] = nome
    print("Aluno adicionado com sucesso!")

def remover_aluno():
    matricula = input("Digite o número de matrícula do aluno a ser removido: ")
    if matricula in alunos:
        del alunos[matricula]
        print("Aluno removido com sucesso!")
    else:
        print("Aluno não encontrado.")

def atualizar_aluno():
    matricula = input("Digite o número de matrícula do aluno a ser atualizado: ")
    if matricula in alunos:
        novo_nome = input("Digite o novo nome do aluno: ")
        alunos[matricula] = novo_nome
        print("Aluno atualizado com sucesso!")
    else:
        print("Aluno não encontrado.")

def ver_alunos():
    print("Lista de Alunos:")
    for matricula, nome in alunos.items():
        print("Matrícula:", matricula, "- Nome:", nome)

def menu():
    while True:
        print("\n----- Menu -----")
        print("1. Adicionar Aluno")
        print("2. Remover Aluno")
        print("3. Atualizar Aluno")
        print("4. Ver Alunos")
        print("5. Sair")
        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            adicionar_aluno()
        elif opcao == "2":
            remover_aluno()
        elif opcao == "3":
            atualizar_aluno()
        elif opcao == "4":
            ver_alunos()
        elif opcao == "5":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Digite novamente.")

# Executar o programa
menu()
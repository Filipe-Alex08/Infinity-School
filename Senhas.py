"""
Faça um programa em python que determine em duas variáveis (senha e email) e que contenha uma senha e um email cadastrados antecipadamente, em seguida solicite ao usuário uma senha e um email e utilize o laço de repetição juntamente com a estrutura de condição para verificar se o email e a senha digitado pelo usuário é igual ao email e senha cadastrados antecipadamente.
E enquanto a senha e o email que o usuário digitou não for igual ao email e senha cadastrados ele continue em um loop.
"""

# Dados 
email_cadas = "aluno_123@email.com"
senha_cadas = "12345678"

while True:
    email = input("Digite o email: ")
    senha = input("Digite a senha: ")
    if email == email_cadas and senha == senha_cadas:
        print("Seja bem vindo! Login realizado!! ")
        break
    else:
        print("Email/senha incorretos. Tentar novamente" )
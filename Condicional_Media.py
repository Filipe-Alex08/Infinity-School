"""Desenvolva um programa em Python que permita ao usuário digitar várias notas. 
Em seguida, crie uma função chamada "calcular_media" que irá receber as notas digitadas e calcular a média do aluno. 
Também crie uma função chamada "verificar_situacao" que, com base na média calculada, irá exibir a situação do aluno: "Reprovado" se a média for menor que 7, "Aprovado" se a média for maior ou igual a 7, e "Parabéns, sua média é 10" se a média for igual a 10.
"""

def calcular_media(notas):
    total_notas = sum(notas)
    quantidade_notas = len(notas)
    media = total_notas / quantidade_notas
    return media

def verificar_situacao(media):
    if media < 7:
        return "Reprovado"
    elif media == 10:
        return "Parabéns, sua média é 10"
    else:
        return "Aprovado"

def main():
    notas = []
    while True:
        try:
            nota = float(input("Digite uma nota (ou -1 para encerrar): "))
            if nota == -1:
                break
            notas.append(nota)
        except ValueError:
            print("Por favor, digite um valor numérico válido.")

    if notas:
        media_aluno = calcular_media(notas)
        situacao = verificar_situacao(media_aluno)
        print(f"Média do aluno: {media_aluno:.2f}")
        print(f"Situação: {situacao}")
    else:
        print("Nenhuma nota foi digitada. Encerrando o programa.")

if __name__ == "__main__":
    main()
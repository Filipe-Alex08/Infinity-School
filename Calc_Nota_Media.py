def media_calcular(notas):
    if not notas:
        return 0.0
    soma = sum(notas)
    media = soma / len(notas)
    return media

notas = []
while True:
    entrada = input('Digite a nota do aluno (ou digite i para encerrar): ')
    if entrada.lower() == 'i':
        break
    try:
        nota = float(entrada)
        notas.append(nota)
    except ValueError:
        print('Insira um valor válido.') 

for i, nota in enumerate(notas, start=1):
    print(f'Média do aluno {i}: {nota:.2f}')

media_geral = media_calcular(notas)
print(f'Média geral da turma: {media_geral:.2f}')
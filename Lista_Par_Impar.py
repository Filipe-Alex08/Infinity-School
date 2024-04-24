# Faça um programa que solicite ao usuário que digite 10 valores para preencher uma lista.
# Em seguida, o programa deve separar os números pares e ímpares em listas diferentes.
# Por fim, exiba na tela os números pares, os números ímpares em uma tupla, a quantidade de números pares e ímpares presentes na lista, e a soma de todos os números pares e ímpares, respectivamente.

numeros = []
numeros_pares = []
numeros_impares = []

print('Você terá que digitar 10 numeros por vez')
print('E iremos dizer quais são numeros impares e quais são numeros par')
# Solicitar ao usuario 10 valores

for _ in range(10):
    numero =int(input("Digite um número:" ) )
    numeros.append(numero)
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)
  

# Exibir os numeros pares
print("Numeros pares:", numeros_pares)

# Exibir os numeros impares em uma tupla
print("Numeros impares:", tuple(numeros_impares))

# Exibir a quantidade de numeros pares e impares
soma_pares = sum(numeros_pares)
soma_impares = sum(numeros_impares)

#Exibir a soma dos numeros pares e impares
print("Soma dos numeros pares:", soma_pares)
print("Soma dos numeros impares:", soma_impares)
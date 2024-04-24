# Desenvolva uma calculadora simples utilizando a biblioteca Tkinter em Python.
# A calculadora deve permitir a realização das operações básicas (adição, subtração, multiplicação e divisão) e ser capaz de lidar com entradas de números inteiros e decimais.
# Além disso, a interface da calculadora deve ser intuitiva e fácil de usar para o usuário.

import tkinter as tk

def button(valor):
    entrada.insert(tk.END, valor)

def calcular():
    try:
        expressao = entrada.get()
        resultado = eval(expressao)
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except:        
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Erro")

def limpar():
    entrada.delete(0, tk.END)

# Cria a janela da calculadora
janela = tk.Tk()
janela.title("Calculadora Simples")
janela.geometry('150x150')
janela.resizable(False, False)

# Cria a entrada de texto
entrada = tk.Entry(janela, width=20)
entrada.grid(row=0, column=0, columnspan=4)

# Cria os botões numéricos
for i in range(10):
    if i == 0:
        tk.Button(janela, text="0", command=lambda valor=i: button(str(valor))).grid(row=4, column=1)
    else:
        row_num = (i - 1) // 3 + 1
        col_num = (i - 1) % 3
        tk.Button(janela, text=str(i), command=lambda valor=i: button(str(valor))).grid(row=row_num, column=col_num)

# Cria os botões de operação
operadores = ['+', '-', '*', '/']
for i, operador in enumerate(operadores):
    tk.Button(janela, text=operador, command=lambda valor=operador: button(valor)).grid(row=i+1, column=3)

# Botões especiais
tk.Button(janela, text=".", command=lambda valor=".": button(valor)).grid(row=4, column=0)
tk.Button(janela, text="=", command=calcular).grid(row=4, column=2)
tk.Button(janela, text="C", command=limpar).grid(row=5, column=0)

# Inicia o loop principal da interface gráfica
janela.mainloop()
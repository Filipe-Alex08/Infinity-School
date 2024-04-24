# Tkinter I

import tkinter as tk
def converter():
    try:
        centimetros = float(entrada_centimetros.get())
        metros = centimetros / 100
        resultado.config(text=f"Equivalente em metros: {metros:.2f} m")
    except ValueError:
        resultado.config(text="Por favor, insira um número válido.")

# Criação da janela principal
janela = tk.Tk()
janela.title("Conversor de Centímetros para Metros")
janela.geometry("300x150")

# Rótulo e entrada para inserir a medida em centímetros
label_centimetros = tk.Label(janela, text="Digite a medida em centímetros:")
label_centimetros.pack(pady=10)
entrada_centimetros = tk.Entry(janela)
entrada_centimetros.pack()

# Botão para realizar a conversão
botao_converter = tk.Button(janela, text="Converter", command=converter)
botao_converter.pack(pady=10)

# Rótulo para exibir o resultado da conversão
resultado = tk.Label(janela, text="")
resultado.pack()

# Iniciar a interface gráfica
janela.mainloop()
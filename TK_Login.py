# Tkinter II
"""
Usando seus conhecimentos aprendidos em sala, realize uma interface de login utilizando a biblioteca Tkinter em Python. 
O objetivo é permitir que o usuário faça login somente se a senha tiver mais de 6 dígitos e se o e-mail contiver o caractere "@", ou seja, realizar uma tela de login com restrições de e-mail e senha.
"""

import tkinter as tk

def login():
    email = entry_email.get()
    password = entry_password.get()
    if len(password) <= 6:
        status_label.config(text="Senha deve conter mais de 6 dígitos.")
    elif "@" not in email:
        status_label.config(text="E-mail inválido.")
    else:
        status_label.config(text="Login realizado com sucesso!")

# Criação da janela
root = tk.Tk()
root.title("Login")

# Widgets
label_email = tk.Label(root, text="E-mail:")
label_email.pack()
entry_email = tk.Entry(root)
entry_email.pack()
label_password = tk.Label(root, text="Senha:")
label_password.pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()
login_button = tk.Button(root, text="Login", command=login)
login_button.pack()
status_label = tk.Label(root, text="")
status_label.pack()

# Execução da interface
root.mainloop()
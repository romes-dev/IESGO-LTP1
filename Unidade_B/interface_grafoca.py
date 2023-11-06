import tkinter as tk

def mostrar_mensagem():
    label.config(text="Olá, IESGO!")

# Criar uma janela
janela = tk.Tk()
janela.title("Exemplo de GUI em Python")

# Criar um rótulo
label = tk.Label(janela, text="Bem vindo à interface gráfica de usuário")
label.pack(padx=10, pady=10)

# criar um botão do tipo CTA (Call to action)

botao = tk.Button(janela, text="Clique aqui!", command=mostrar_mensagem)
botao.pack(padx=10, pady=10)
botao.config(width=15, height=20)

# Iniciar a GUI em loop
janela.mainloop()




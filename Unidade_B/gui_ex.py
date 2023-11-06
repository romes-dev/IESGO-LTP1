import tkinter as tk

# Função a ser chamada quando o botão for pressionado
def mostrar_mensagem():
    label.config(text="Olá, Mundo!")

# Criar uma janela
janela = tk.Tk()
janela.title("Exemplo de GUI em Python")

# Criar um rótulo
label = tk.Label(janela, text="Bem-vindo à GUI em Python")
label.pack(padx=10, pady=10)

# Criar um botão
botao = tk.Button(janela, text="Clique Aqui", command=mostrar_mensagem)
botao.pack(padx=10, pady=10)

# Iniciar o loop da GUI
janela.mainloop()

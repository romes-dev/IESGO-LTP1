# Classes em lib Tkinter

# Classes
"""
Tk                # Classe para criar uma janela principal
Toplevel          # Classe para criar janelas secundárias
Frame             # Classe para criar quadros (frames) na interface
Label             # Classe para criar rótulos de texto
Button            # Classe para criar botões
Entry             # Classe para criar campos de entrada de texto
Text              # Classe para criar áreas de texto
Canvas            # Classe para criar áreas de desenho
Checkbutton       # Classe para criar caixas de verificação (checkbuttons)
Radiobutton       # Classe para criar botões de seleção (radiobuttons)
Scale             # Classe para criar barras de rolagem (scales)
Listbox           # Classe para criar listas de seleção
Menu              # Classe para criar menus
Scrollbar         # Classe para criar barras de rolagem
Combobox          # Classe para criar listas suspensas (comboboxes)
Message           # Classe para criar caixas de mensagem
MessageBox        # Classe para exibir caixas de diálogo
...
# Métodos

mainloop()        # Método para iniciar o loop da GUI
after()           # Método para agendar chamadas de função após um período de tempo
bind()            # Método para vincular eventos a funções
pack()            # Método para gerenciamento de geometria usando empacotamento
grid()            # Método para gerenciamento de geometria usando uma grade
place()           # Método para gerenciamento de geometria usando posicionamento absoluto
...
# Constantes
LEFT, RIGHT, TOP, BOTTOM  # Constantes para especificar a direção do empacotamento
YES, NO, BOTH             # Constantes para especificar como o widget deve se expandir

"""
import tkinter as tk
from tkinter import messagebox
import pesquisar_produto


def abrir_janela(mensagem):
    nova_janela = tk.Toplevel()
    nova_janela.title("Ação qualquer...")
    
    label = tk.Label(nova_janela, text=mensagem, padx=20, pady=20)
    label.pack()
    
    botao_fechar = tk.Button(nova_janela, text="SAIR", command=nova_janela.destroy)
    botao_fechar.pack(padx=20, pady=10)

# Funções para as diferentes funcionalidades do sistema ERP

def pesquisar_produto():
    abrir_janela("Pesquisar Produto")

def checar_estoque():
    abrir_janela("Checar estoque")

def acrescentar_estoque():
    abrir_janela("Acrescentar Estoque")

def remover_estoque():
    abrir_janela("Remover do estoque")
    
def cadastrar_produto():
    abrir_janela("Cadastrar produto")

# Criar a janela principal

janela_principal = tk.Tk()
janela_principal.title("SISTEMA ERP IESGO")
janela_principal.attributes('-fullscreen', True)

# iconfinder.com
# Configurar ícones do menu
icon_pesquisar = tk.PhotoImage(file="/Users/romes/Documents/GitHub/IESGO-LTP1/Unidade_B/pesquisar.png")
icon_estoque = tk.PhotoImage(file="/Users/romes/Documents/GitHub/IESGO-LTP1/Unidade_B/estoque.png")
icon_acrescentar = tk.PhotoImage(file="/Users/romes/Documents/GitHub/IESGO-LTP1/Unidade_B/add.png")
icon_remover = tk.PhotoImage(file="/Users/romes/Documents/GitHub/IESGO-LTP1/Unidade_B/remover.png")
icon_cadastrar = tk.PhotoImage(file="/Users/romes/Documents/GitHub/IESGO-LTP1/Unidade_B/cadastrar.png")

# Criar botões com ícones
botao_pesquisar = tk.Button(janela_principal, image=icon_pesquisar, command=pesquisar_produto)
botao_estoque = tk.Button(janela_principal, image=icon_estoque, command=checar_estoque)
botao_acrescentar = tk.Button(janela_principal, image=icon_acrescentar, command=acrescentar_estoque)
botao_remover = tk.Button(janela_principal, image=icon_remover, command=remover_estoque)
botao_cadastrar = tk.Button(janela_principal, image=icon_cadastrar, command=cadastrar_produto)

#Exibir os botões na janela
botao_pesquisar.pack()
botao_estoque.pack()
botao_acrescentar.pack()
botao_remover.pack()
botao_acrescentar.pack()

# Loop da janela principal
janela_principal.mainloop()


# PRograma com registro de nome e emails.

import sqlite3
import tkinter as tk
from tkinter import ttk

# Criar um banco de dados SQLite e uma tabela de usuários
conn = sqlite3.connect('user_database.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')
conn.commit()

class AplicativoGestaoUsuarios:
    def __init__(self, root):
        self.root = root
        self.root.title("App de Gestão de Usuários")

        self.tree = ttk.Treeview(root, columns=('ID', 'Username', 'Email'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Username', text='Usuário')
        self.tree.heading('Email', text='E-mail')
        self.tree.pack(padx=10, pady=10)

        self.carregar_dados()

        botao_adicionar = tk.Button(root, text='Adicionar', command=self.mostrar_janela_adicionar_usuario)
        botao_adicionar.pack(pady=10)

        botao_remover = tk.Button(root, text='Remover', command=self.remover_usuario)
        botao_remover.pack(pady=10)

    def carregar_dados(self):
        # Buscar dados do banco de dados e popular o treeview
        cursor.execute('SELECT * FROM users')
        linhas = cursor.fetchall()
        for linha in linhas:
            self.tree.insert('', 'end', values=linha)

    def mostrar_janela_adicionar_usuario(self):
        janela_adicionar_usuario = tk.Toplevel(self.root)
        janela_adicionar_usuario.title('Adicionar Usuário')

        rotulo_usuario = tk.Label(janela_adicionar_usuario, text='Usuário:')
        rotulo_usuario.grid(row=0, column=0, padx=10, pady=10)
        entrada_usuario = tk.Entry(janela_adicionar_usuario)
        entrada_usuario.grid(row=0, column=1, padx=10, pady=10)

        rotulo_email = tk.Label(janela_adicionar_usuario, text='E-mail:')
        rotulo_email.grid(row=1, column=0, padx=10, pady=10)
        entrada_email = tk.Entry(janela_adicionar_usuario)
        entrada_email.grid(row=1, column=1, padx=10, pady=10)

        botao_salvar = tk.Button(janela_adicionar_usuario, text='Salvar', command=lambda: self.salvar_usuario(entrada_usuario.get(), entrada_email.get(), janela_adicionar_usuario))
        botao_salvar.grid(row=2, columnspan=2, pady=10)

    def salvar_usuario(self, usuario, email, janela):
        # Salvar usuário no banco de dados
        cursor.execute('INSERT INTO users (username, email) VALUES (?, ?)', (usuario, email))
        conn.commit()

        # Atualizar o treeview com o novo usuário
        self.tree.insert('', 'end', values=(cursor.lastrowid, usuario, email))

        # Fechar a janela de adicionar usuário
        janela.destroy()

    def remover_usuario(self):
        item_selecionado = self.tree.selection()
        if item_selecionado:
            id_usuario = self.tree.item(item_selecionado)['values'][0]
            cursor.execute('DELETE FROM users WHERE id=?', (id_usuario,))
            conn.commit()

            # Remover o usuário selecionado do treeview
            self.tree.delete(item_selecionado)
        else:
            tk.messagebox.showinfo('Erro', 'Selecione um usuário para remover da lista.')

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicativoGestaoUsuarios(root)
    root.mainloop()

# Fechar a conexão com o banco de dados quando a aplicação for fechada
conn.close()

# PRograma GUI com registro de nome e foto de usuário
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sqlite3
from PIL import Image, ImageTk

class ClienteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Clientes")

        # Conectar ao banco de dados SQLite
        self.conn = sqlite3.connect('clientes_database.db')
        self.cursor = self.conn.cursor()

        # Criar a tabela se ela não existir
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                foto BLOB
            )
        ''')
        self.conn.commit()

        # Interface gráfica
        self.create_widgets()

    def create_widgets(self):
        # Nome do Cliente
        self.nome_label = tk.Label(self.root, text='Nome:')
        self.nome_label.grid(row=0, column=0, padx=10, pady=10)
        self.nome_entry = tk.Entry(self.root)
        self.nome_entry.grid(row=0, column=1, padx=10, pady=10)

        # Foto do Cliente
        self.foto_label = tk.Label(self.root, text='Foto:')
        self.foto_label.grid(row=1, column=0, padx=10, pady=10)

        # Botão para adicionar foto
        self.adicionar_foto_button = tk.Button(self.root, text='Adicionar Foto', command=self.adicionar_foto)
        self.adicionar_foto_button.grid(row=1, column=1, padx=10, pady=10)

        # Botão para cadastrar cliente
        self.cadastrar_cliente_button = tk.Button(self.root, text='Cadastrar Cliente', command=self.cadastrar_cliente)
        self.cadastrar_cliente_button.grid(row=2, columnspan=2, pady=10)

        # Treeview para exibir os clientes
        self.tree = ttk.Treeview(self.root, columns=('ID', 'Nome', 'Foto'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Nome', text='Nome')
        self.tree.heading('Foto', text='Foto')
        self.tree.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Atualizar a visualização dos clientes
        self.update_clientes_view()

    def adicionar_foto(self):
        filename = filedialog.askopenfilename(initialdir='/', title='Escolha um arquivo',
                                      filetypes=[('Imagens', '*.png;*.gif;*.ppm;*.jpg')])

        if filename:
            self.foto_path = filename
            self.mostrar_foto()

    def mostrar_foto(self):
        try:
            foto = Image.open(self.foto_path)
            foto.thumbnail((50, 50))  # Ajuste o tamanho conforme necessário
            foto = ImageTk.PhotoImage(foto)
            self.foto_label.config(image=foto)
            self.foto_label.image = foto  # Mantenha uma referência para evitar que a imagem seja coletada pelo garbage collector
        except Exception as e:
            messagebox.showerror('Erro', f'Erro ao abrir a foto: {e}')

    def cadastrar_cliente(self):
        nome = self.nome_entry.get()

        if not nome:
            messagebox.showwarning('Aviso', 'Por favor, insira o nome do cliente.')
            return

        # Converter a foto para bytes
        if hasattr(self, 'foto_path'):
            with open(self.foto_path, 'rb') as file:
                foto_blob = file.read()
        else:
            foto_blob = None

        # Inserir cliente no banco de dados
        self.cursor.execute('INSERT INTO clientes (nome, foto) VALUES (?, ?)', (nome, foto_blob))
        self.conn.commit()

        # Limpar os campos de entrada
        self.nome_entry.delete(0, tk.END)
        self.foto_label.config(image='')  # Limpar a imagem

        # Atualizar a visualização dos clientes
        self.update_clientes_view()

    def update_clientes_view(self):
        # Limpar as entradas existentes
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Obter todos os clientes do banco de dados
        self.cursor.execute('SELECT * FROM clientes')
        clientes = self.cursor.fetchall()

        # Adicionar clientes à Treeview
        for cliente in clientes:
            self.tree.insert('', 'end', values=cliente)

if __name__ == "__main__":
    root = tk.Tk()
    app = ClienteApp(root)
    root.mainloop()

# Fechar a conexão com o banco de dados quando a aplicação for encerrada
app.conn.close()

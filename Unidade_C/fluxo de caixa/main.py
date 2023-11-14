import tkinter as tk
from tkinter import ttk
import sqlite3
from datetime import datetime

class FinancasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Controle de Finanças Pessoais")

        # Conectar ao banco de dados SQLite
        self.conn = sqlite3.connect('financas_database.db')
        self.cursor = self.conn.cursor()

        # Criar a tabela se ela não existir
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transacoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL,
                valor REAL NOT NULL,
                data DATE NOT NULL,
                tipo TEXT NOT NULL
            )
        ''')
        self.conn.commit()

        # Interface gráfica
        self.create_widgets()

    def create_widgets(self):
        # Descrição
        self.descricao_label = tk.Label(self.root, text='Descrição:')
        self.descricao_label.grid(row=0, column=0, padx=10, pady=10)
        self.descricao_entry = tk.Entry(self.root)
        self.descricao_entry.grid(row=0, column=1, padx=10, pady=10)

        # Valor
        self.valor_label = tk.Label(self.root, text='Valor:')
        self.valor_label.grid(row=1, column=0, padx=10, pady=10)
        self.valor_entry = tk.Entry(self.root)
        self.valor_entry.grid(row=1, column=1, padx=10, pady=10)

        # Tipo
        self.tipo_label = tk.Label(self.root, text='Tipo:')
        self.tipo_label.grid(row=2, column=0, padx=10, pady=10)
        self.tipo_combobox = ttk.Combobox(self.root, values=['Receber', 'Pagar'])
        self.tipo_combobox.grid(row=2, column=1, padx=10, pady=10)
        self.tipo_combobox.set('Receber')  # Valor padrão

        # Data
        self.data_label = tk.Label(self.root, text='Data (DD-MM-YYYY):')
        self.data_label.grid(row=3, column=0, padx=10, pady=10)
        self.data_entry = tk.Entry(self.root)
        self.data_entry.grid(row=3, column=1, padx=10, pady=10)

        # Botão Adicionar
        self.adicionar_button = tk.Button(self.root, text='Adicionar Transação', command=self.adicionar_transacao)
        self.adicionar_button.grid(row=4, columnspan=2, pady=10)

        # Treeview para exibir as transações
        self.tree = ttk.Treeview(self.root, columns=('ID', 'Descrição', 'Valor', 'Data', 'Tipo'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Descrição', text='Descrição')
        self.tree.heading('Valor', text='Valor')
        self.tree.heading('Data', text='Data')
        self.tree.heading('Tipo', text='Tipo')
        self.tree.grid(row=5, column=0, columnspan=2, padx=10, pady=10)  # Use grid instead of pack

        # Rótulo para exibir o saldo
        self.saldo_label = tk.Label(self.root, text='Saldo: R$ 0.00')
        self.saldo_label.grid(row=6, column=0, columnspan=2, pady=10)

        # Atualizar a visualização das transações e o saldo
        self.update_transacoes_view()

    def adicionar_transacao(self):
        # Obter dados do usuário
        descricao = self.descricao_entry.get()
        valor = float(self.valor_entry.get())
        tipo = self.tipo_combobox.get()
        data_str = self.data_entry.get()

        # Validar e converter a data para o formato SQLite
        try:
            data = datetime.strptime(data_str, '%d-%m-%Y').date()
        except ValueError:
            tk.messagebox.showerror('Erro', 'Formato de data inválido. Use DD-MM-YYYY.')
            return

        # Inserir transação no banco de dados
        self.cursor.execute('INSERT INTO transacoes (descricao, valor, data, tipo) VALUES (?, ?, ?, ?)',
                            (descricao, valor, data, tipo))
        self.conn.commit()

        # Limpar os campos de entrada
        self.descricao_entry.delete(0, tk.END)
        self.valor_entry.delete(0, tk.END)
        self.tipo_combobox.set('Receber')
        self.data_entry.delete(0, tk.END)

        # Atualizar a visualização das transações
        self.update_transacoes_view()
        

    def update_transacoes_view(self):
         # Limpar as entradas existentes
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Obter todas as transações do banco de dados
        self.cursor.execute('SELECT * FROM transacoes')
        transacoes = self.cursor.fetchall()

        # Adicionar transações à Treeview
        for transacao in transacoes:
            self.tree.insert('', 'end', values=transacao)

        # Calcular e exibir o saldo
        saldo = self.calcular_saldo(transacoes)
        self.saldo_label.config(text=f'Saldo: R$ {saldo:.2f}')

    def calcular_saldo(self, transacoes):
        saldo = 0
        for transacao in transacoes:
            if transacao[4] == 'Receber':
                saldo += transacao[2]  # Adiciona ao saldo se for uma entrada
            else:
                saldo -= transacao[2]  # Subtrai do saldo se for uma saída
        return saldo

if __name__ == "__main__":
    root = tk.Tk()
    app = FinancasApp(root)
    root.mainloop()

# Fechar a conexão com o banco de dados quando a aplicação for encerrada
app.conn.close()

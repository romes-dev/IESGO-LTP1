import sqlite3
import tkinter as tk
from tkinter import ttk

# Create a SQLite database and a users table
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

class UserManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("App de Gestão de Usuários")

        self.tree = ttk.Treeview(root, columns=('ID', 'Username', 'Email'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Username', text='Usuário')
        self.tree.heading('Email', text='E-mail')
        self.tree.pack(padx=10, pady=10)

        self.load_data()

        add_button = tk.Button(root, text='Adicionar', command=self.show_add_user_window)
        add_button.pack(pady=10)

        delete_button = tk.Button(root, text='Remover', command=self.delete_user)
        delete_button.pack(pady=10)

    def load_data(self):
        # Fetch data from the database and populate the treeview
        cursor.execute('SELECT * FROM users')
        rows = cursor.fetchall()
        for row in rows:
            self.tree.insert('', 'end', values=row)

    def show_add_user_window(self):
        add_user_window = tk.Toplevel(self.root)
        add_user_window.title('Add User')

        username_label = tk.Label(add_user_window, text='Username:')
        username_label.grid(row=0, column=0, padx=10, pady=10)
        username_entry = tk.Entry(add_user_window)
        username_entry.grid(row=0, column=1, padx=10, pady=10)

        email_label = tk.Label(add_user_window, text='Email:')
        email_label.grid(row=1, column=0, padx=10, pady=10)
        email_entry = tk.Entry(add_user_window)
        email_entry.grid(row=1, column=1, padx=10, pady=10)

        save_button = tk.Button(add_user_window, text='Save', command=lambda: self.save_user(username_entry.get(), email_entry.get(), add_user_window))
        save_button.grid(row=2, columnspan=2, pady=10)

    def save_user(self, username, email, window):
        # Save user to the database
        cursor.execute('INSERT INTO users (username, email) VALUES (?, ?)', (username, email))
        conn.commit()

        # Update the treeview with the new user
        self.tree.insert('', 'end', values=(cursor.lastrowid, username, email))

        # Close the add user window
        window.destroy()

    def delete_user(self):
        selected_item = self.tree.selection()
        if selected_item:
            user_id = self.tree.item(selected_item)['values'][0]
            cursor.execute('DELETE FROM users WHERE id=?', (user_id,))
            conn.commit()

            # Remove the selected user from the treeview
            self.tree.delete(selected_item)
        else:
            tk.messagebox.showinfo('Error', 'Selcione um usuário para remover da lista.')

if __name__ == "__main__":
    root = tk.Tk()
    app = UserManagementApp(root)
    root.mainloop()

# Close the database connection when the application is closed
conn.close()

import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser

class SistemaGestaoEscolar:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestão Escolar")

        # Adicione os caminhos corretos para seus arquivos PNG
        self.icones = [
            "pesquisar.png",
            "cadastrar_aspirante.png",
            "cadastrar.png",
            "visualizar_turmas.png",
            "registro_frequencia.png",
        ]

        # Criar um notebook com duas guias
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Guia para os ícones
        self.guia_icones = ttk.Frame(self.notebook)
        self.notebook.add(self.guia_icones, text="Ícones")

        # Calcular o tamanho inicial dos ícones
        self.atualizar_tamanho_icones()

        # Adicione ícones à guia de ícones
        for icone_nome in self.icones:
            caminho_icone = os.path.join(os.path.dirname(__file__), icone_nome)
            imagem = Image.open(caminho_icone)
            imagem = imagem.resize(self.tamanho_icone, Image.ANTIALIAS)
            icone = ImageTk.PhotoImage(imagem)

            botao = tk.Button(self.guia_icones, image=icone, command=lambda i=icone: self.clicar_botao(i))
            botao.image = icone
            botao.pack(side=tk.LEFT, fill=tk.X, padx=5, pady=5, expand=True)

        # Guia para incorporar o vídeo do YouTube
        self.guia_video = ttk.Frame(self.notebook)
        self.notebook.add(self.guia_video, text="Vídeo")

        # Botão para abrir o vídeo no navegador
        botao_video = tk.Button(self.guia_video, text="Abrir Vídeo", command=self.abrir_video)
        botao_video.pack(pady=10)

    def clicar_botao(self, icone):
        # Adicione a lógica para cada botão aqui
        print("Botão clicado!")

    def abrir_video(self):
        webbrowser.open("https://youtu.be/NCEZIStN72s?si=VPbZZn30PW7f0hTr")

    def atualizar_tamanho_icones(self):
        # Calcular o tamanho relativo com base na largura da janela
        largura_janela = self.root.winfo_width()
        tamanho_icone = int(largura_janela / 20)  # Ajuste conforme necessário
        self.tamanho_icone = (tamanho_icone, tamanho_icone)

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaGestaoEscolar(root)
    root.mainloop()

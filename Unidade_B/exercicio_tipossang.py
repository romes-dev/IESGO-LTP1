# Inicializar uma lista de tipos sang vazia

lista_de_pessoas = []

# Nome do arquivo onde vamos carregar os dados

nome_do_arquivo = "lista_tipos_sanguineos.txt"

# Adicionar nomes a lista

def adicionar_nome_e_tipo_sanguineo():
    nome = input("Digite o nome do paciente: ")
    tipo_sanguineo = input("Digite o tipo sanguíneo: ")
    pessoa = {
        "Nome": nome,
        "Tipo Sanguíneo": tipo_sanguineo
    }
    lista_de_pessoas.append(pessoa)
    print(f"Dados de {pessoa} armazenados com sucesso!")

# Visualizar a lista de pacientes

def visualizar_lista():
    if not lista_de_pessoas:
        print("A lista está vazia")
    else:
        print("Lista de Nomes e Tipagem Sanguínea:")
        for pessoa in lista_de_pessoas:
            print(
                f"Nome: {pessoa['Nome']}, Tipo Sanguíneo: {pessoa['Tipo Sanguíneo']}"
            )

# Salvar os dados em um arquivo txt
def salvar_dados():
    with open(nome_do_arquivo, "w") as arquivo:
        for pessoa in lista_de_pessoas:
            arquivo.write(
                f"Nome: {pessoa['Nome']}, Tipo Sanguíneo: {pessoa['Tipo Sanguíneo']}"
            )
        print("Arquivo gerado com sucesso!")

#Carregar dados
def carregar_dados():
    try:
        with open(nome_do_arquivo, "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(", ")
                nome = dados[0].split(": ")[1]
                tipo_sanguineo = dados[1].split(": ")[1]
                pessoa = {
                    "Nome": nome,
                    "Tipo Sanguíneo": tipo_sanguineo
                }
                lista_de_pessoas.append(pessoa)
            print("Dados carregados com sucesso!")
    except FileNotFoundError:
        print(f"ERRO! \n O arquivo {nome_do_arquivo} não foi encontrado. Contate o administrador do sistema.")
    
carregar_dados()

#Menu principal
while True:
    print("\n Opções")
    print(
        "1. ADICIONAR PACIENTE E TIPO SANGUÍNEO \n2. VISUALIZAR PACIENTES \n3. SALVAR DADOS EM ARQUIVO \n4. ENCERRAR O SISTEMA"
    )
    opcao = input("ESCOLHA UMA OPÇÃO: ")
    if opcao == "1":
        adicionar_nome_e_tipo_sanguineo()
    elif opcao == "2":
        visualizar_lista()
    elif opcao == "3":
        salvar_dados()
    elif opcao == "4":
        print("Sistema encerrado com sucesso!")
        break
    else:
        print("Opção inválida, tente novamente!")

        
        
    
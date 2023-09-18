
# Exercicio 4: Faça um programa que solicita ao usuário escrever o nome das frutas que ele deseja comprar. O usuário deve digitar as frutas até digitar a palavra "sair". O programa deve imprimir na tela a lista de frutas que o usuário deseja comprar.

def lista_de_compras():
    lista = []
    fruta = input("Digite o nome da fruta que deseja comprar ou 'sair' para sair: ").lower()
    while fruta != "sair":
        lista.append(fruta)
        print(lista)
        fruta = input("Digite o nome da fruta que deseja comprar ou 'sair' para sair: ").lower()
    print(f"Lista de compras: \n {lista}")
    return lista

lista_de_compras()
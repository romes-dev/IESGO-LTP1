
# Exercício 3: Crie um programa em que o usuário insira uma palavra e o programa retorna se a palavra é palíndromo ou não.

def palindromo():
    nome = input("Digite um nome: ")
    if nome == nome[::-1]:
        print("É palíndromo")
    else:
        print("Não é palíndromo")

palindromo()
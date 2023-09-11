# Exercício com range e if em python

# Crie um programa que solicite ao usuário inserir um número inteiro positivo e o sistema retorna se ele é múltiplo de 5 e retorne uma lista de todos os números positivos menores que o número inserido que são múltiplos de 5.

# Checar se é múltiplo de 5

def checagem_multiplo_5(numero_checagem):
    if numero_checagem % 5 == 0:
        print(f"O número {numero_checagem} é múltiplo de 5.")
        return True
    else:
        print(f"O número {numero_checagem} não é múltiplo de 5.")
        return False

# Solicitar ao usuário inserir um número inteiro positivo

def solicitar_numero():
    numero_inserido = input("Digite um número inteiro positivo: ")
    if numero_inserido == "":
        print("Você não digitou um número.")
        return solicitar_numero()
    elif numero_inserido.isalpha():
        print("Você não digitou um número.")
        return solicitar_numero()
    elif int(numero_inserido) < 0:
        print("Você não digitou um número positivo.")
        return solicitar_numero()
    else:
        return int(numero_inserido)
    



# Lista de múltiplos de 5 menores ou iguais ao número inserido

def lista_multiplos_5(numero):
    lista = []
    for i in range(numero+1):
        if checagem_multiplo_5(i):
            lista.append(i)
    return lista


def sistema_de_checagem():
    numero = solicitar_numero()
    lista = lista_multiplos_5(numero)
    print(f"Os números menores ou iguais a {numero} que são múltiplos de 5 são: {lista}")

sistema_de_checagem()
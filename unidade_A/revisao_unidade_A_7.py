# Praticando com o comando if

# Programa que solicita ao usuário inserir um número inteiro e retorna se o número é par ou ímpar.

def par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

numero = int(input("Digite um número inteiro: "))
print(f"O número {numero} é {par_ou_impar(numero)}.")

# Programa que solicita ao usuário inserir um número inteiro e retorna se ele é múltiplo de 5.

def multiplo_de_5(numero):
    if numero % 5 == 0:
        return True
    else:
        return False

numero = int(input("Digite um número inteiro: "))
if multiplo_de_5(numero):
    print(f"O número {numero} é múltiplo de 5.")
else:
    print(f"O número {numero} não é múltiplo de 5.")

# Programa que solicita ao usuário inserir um número inteiro e retorna se ele é múltiplo de 5 e de 3.

def multiplo_de_5_e_3(numero):
    if numero % 5 == 0 and numero % 3 == 0:
        return True
    else:
        return False

numero = int(input("Digite um número inteiro: "))
if multiplo_de_5_e_3(numero):
    print(f"O número {numero} é múltiplo de 5 e de 3.")
else:
    print(f"O número {numero} não é múltiplo de 5 e de 3.")

# Programa para idenficar se uma palavra é palíndromo.

def palindromo(palavra):
    if palavra == palavra[::-1]:
        return True
    else:
        return False

palavra = input("Digite uma palavra: ")
if palindromo(palavra):
    print(f"A palavra {palavra} é um palíndromo.")
else:
    print(f"A palavra {palavra} não é um palíndromo.")
    
# Programa que solicita ao usuário inserir um número inteiro e retorna se ele é primo.

def primo(numero):
    if numero <= 1:
        return False
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True

numero = int(input("Digite um número inteiro: "))
if primo(numero):
    print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} não é primo.")
    
# Programa para retornar o fatorial de um número.

numero = int(input("Digite um número inteiro: "))
fatorial = 1
for i in range(1, numero + 1):
    fatorial *= i
print(f"O fatorial de {numero}! é {fatorial}.")

# Programa para definir se elementos de uma lista são menores que 10.

lista = [1, 3, 4, 5, 6, 10, 12, 14, 144, 200, 1222, 5000, 100000]
nova_lista = []

def checagem_de_lista(lista):
    for i in lista:
        if i <= 5:
            nova_lista.append(i)
        else:
            pass

checagem_de_lista(lista)
print(nova_lista)
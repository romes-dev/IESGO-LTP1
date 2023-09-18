 
# Exercício 2: Faça uma função que recebe um número e imprime no console se ele é múltiplo de 5 e de 3 ou False caso contrário.

def multiplo_de_5(numero):
    if numero % 5 == 0:
        return True
    else:
        return False

def multiplo_de_3(numero):
    if numero % 3 == 0:
        return True
    else:
        return False

def multiplo_de_5_e_3(numero):
    if multiplo_de_5(numero) and multiplo_de_3(numero):
        return True
    else:
        return False

numero = int(input("Digite um número: "))
print(multiplo_de_5_e_3(numero))



# Exercício 7: Faça um programa que solicita ao usuário inserir um número inteiro e retorna se ele é primo.

# Um número é primo quando é divisível apenas por 1 e por ele mesmo. Por exemplo, 2, 3, 5 e 7 são números primos, mas 4, 6, 8 e 9 não são.

def eh_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    else:
        for num in range(2, numero):
            if numero % num == 0:
                return False
        return True
    
numero = int(input("Digite um número inteiro: ")) 
print(eh_primo(numero))

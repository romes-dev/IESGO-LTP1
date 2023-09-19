import random as rd

# Exercício 9: Usando o método random(), crie um programa que solicita ao usuário que adivinhe um número inteiro entre 1 e 10 (contando o 10). Se o usuário digitar um número menor que 1 ou maior que 10, solicite que ele insira um número válido. Se o usuário digitar um número válido, verifique se o número que o usuário digitou é igual ao número gerado aleatoriamente pelo programa. Se o número for igual, imprima "Você acertou!". Caso contrário, imprima "Você errou!".

# Extra: Conte quantas tentativas o usuário precisou para acertar o número. Permita tentativas até o usuário acertar o número.

def jogo_de_advinhacao(numero):
    numero_de_tentativas = 1
    numero_sorteado = rd.randint(1, 11)
    while numero < 1 or numero > 10:
        print("Número inválido.")
        numero = int(input("Digite um número inteiro entre 1 e 10: "))
    else:
        print("Número válido.")
    while numero != numero_sorteado:
        numero_de_tentativas += 1
        print("Você errou!")
        numero = int(input("Digite um número inteiro entre 1 e 10: "))
    print(f"Você acertou! O número sorteado foi {numero_sorteado}. Você precisou de {numero_de_tentativas} tentativas para acertar o número.")
    
    

numero = int(input("Digite um número inteiro entre 1 e 10: "))
jogo_de_advinhacao(numero)
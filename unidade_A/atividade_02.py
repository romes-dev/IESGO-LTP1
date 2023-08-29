### Desafio... Jogo de advinhação
### 1. O computador vai "pensar" em um número entre 0 e 10. O jogador vai tentar advinhar qual número foi escolhido até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""
import random
import time
 # vamos usar o método Randit para gerar um número aleatório entre 0 e 10
numero_sorteado = random.randint(0, 10)
print("O computador está sorteando um número entre 0 e 10.")
time.sleep(1)
print("O computador está sorteando um número entre 0 e 10..")
time.sleep(1)
print("O computador está sorteando um número entre 0 e 10...")
time.sleep(1)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')

# Jogo de advinhação
acertou = False
palpites = 0
while acertou == False:
    palpite_do_jogador = int(input('Qual é o seu palpite (número de 0 a 10)? '))
    if palpite_do_jogador == numero_sorteado:
        acertou = True
        print('Parabéns! Você acertou!')
    else:
        palpites += 1
        print('Você errou! Tente novamente.')
print(f'Você precisou de {palpites} palpites para acertar.')

"""
# Papel, pedra e tesoura contra o computador (Jokenpô)
import random

def jokenpo():
    opcoes_do_jogo = ['pedra', 'papel', 'tesoura']
    selecao_do_computador = random.choice(opcoes_do_jogo)
    selecao_do_usuario = opcoes_do_jogo[int(input('Escolha entre pedra, papel ou tesoura: \n 1. pedra \n 2. papel \n 3. tesoura \n'))-1]
    print(f'O computador escolheu {selecao_do_computador}.')
    print(f'O usuário escolheu {selecao_do_usuario}.')

    if selecao_do_usuario == selecao_do_computador:
        print('Empate!')
    elif selecao_do_usuario == 'pedra' and selecao_do_computador == 'tesoura':
        print('Você ganhou!')
    elif selecao_do_usuario == 'papel' and selecao_do_computador == 'pedra':
        print('Você ganhou!')
    elif selecao_do_usuario == 'tesoura' and selecao_do_computador == 'papel':
        print('Você ganhou!')
    else:
        print('Você perdeu!')
    input('Pressione ENTER para jogar novamente...')
    jokenpo()

jokenpo()
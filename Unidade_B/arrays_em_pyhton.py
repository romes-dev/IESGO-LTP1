"""
Exercício: Manipulando um Array

Crie um programa Python que faz o seguinte:

xCrie um array de inteiros vazio.
xPeça ao usuário para inserir 5 números inteiros e adicione esses números ao array.
xExiba o array resultante.
x Calcule a soma de todos os números no array e exiba o resultado.
xEncontre o valor mínimo e o valor máximo no array e exiba ambos.
xRemova o último elemento do array.
x Inverta a ordem dos elementos no array.
Exiba o array após as operações acima
"""

import array as arr 

# Criar um array de inteiros vazio
meu_array = arr.array('i')

# Adicionar cinco no ao array
for i in range(5):
    num = int(input("Insira um número inteiro"))
    meu_array.append(num)

print("Array resultante: ", meu_array)

# Somar os números do array
print(sum(meu_array))

# Encontrar o min e max
min_valor = min(meu_array)
max_valor = max(meu_array)
print(f"O menor valor é: {min_valor}\nO maior valor é: {max_valor}")

# Remover o último elemento
print(meu_array)
meu_array.pop()
print("Removido o último elemento", meu_array)

# Inverter a ordem
meu_array.reverse()
print("lista invertida: ", meu_array)
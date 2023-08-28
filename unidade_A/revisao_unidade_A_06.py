# Operadores Aritméticos: Realizam operações matemáticas básicas.
a = 10
b = 5

soma = a + b  # Adição
subtracao = a - b  # Subtração
multiplicacao = a * b  # Multiplicação
divisao = a / b  # Divisão
resto = a % b  # Resto da divisão
exponenciacao = a ** b  # Exponenciação

print("Operadores Aritméticos:")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
print(f"Resto: {resto}")
print(f"Exponenciação: {exponenciacao}\n")

# Operadores de Atribuição: Usados para atribuir valores a variáveis.
x = 5
x += 3  # Equivalente a x = x + 3
x -= 2  # Equivalente a x = x - 2
x *= 4  # Equivalente a x = x * 4
x /= 2  # Equivalente a x = x / 2

print("Operadores de Atribuição:")
print(f"Valor final de x: {x}\n")

# Operadores de Comparação: Usados para comparar valores.
num1 = 10
num2 = 5

igual = num1 == num2  # Igual a
diferente = num1 != num2  # Diferente de
maior = num1 > num2  # Maior que
menor = num1 < num2  # Menor que
maior_ou_igual = num1 >= num2  # Maior ou igual a
menor_ou_igual = num1 <= num2  # Menor ou igual a

print("Operadores de Comparação:")
print(f"Igual a: {igual}")
print(f"Diferente de: {diferente}")
print(f"Maior que: {maior}")
print(f"Menor que: {menor}")
print(f"Maior ou igual a: {maior_ou_igual}")
print(f"Menor ou igual a: {menor_ou_igual}\n")

# Operadores Lógicos: Usados para combinar condições lógicas.
condicao1 = True
condicao2 = False

e_logico = condicao1 and condicao2  # E lógico (ambas as condições devem ser True)
ou_logico = condicao1 or condicao2  # OU lógico (pelo menos uma condição deve ser True)
nao_logico = not condicao1  # NOT lógico (inverte o valor da condição)

print("Operadores Lógicos:")
print(f"E lógico: {e_logico}")
print(f"OU lógico: {ou_logico}")
print(f"NOT lógico: {nao_logico}\n")

# Operadores de Identidade: Usados para comparar objetos.
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]

identico = lista1 is lista2  # Verifica se os objetos são idênticos
nao_identico = lista1 is not lista2  # Verifica se os objetos não são idênticos

print("Operadores de Identidade:")
print(f"Idêntico: {identico}")
print(f"Não identico: {nao_identico}\n")

# Operadores de Associação: Usados para verificar se um elemento está presente em uma sequência.
frutas = ["maçã", "banana", "cereja"]

verifica_fruta = "banana" in frutas  # Verifica se "banana" está na lista
nao_verifica_fruta = "laranja" not in frutas  # Verifica se "laranja" não está na lista

print("Operadores de Associação:")
print(f"Verifica fruta: {verifica_fruta}")
print(f"Não verifica fruta: {nao_verifica_fruta}\n")

# Operadores Bit a Bit (Bitwise): Realizam operações em nível de bits.
bitwise_and = 5 & 3  # AND bit a bit (101 & 011 = 001)
bitwise_or = 5 | 3  # OR bit a bit (101 | 011 = 111)
bitwise_xor = 5 ^ 3  # XOR bit a bit (101 ^ 011 = 110)
bitwise_not = ~5  # NOT bit a bit (~101 = 010)

print("Operadores Bit a Bit:")
print(f"AND bit a bit: {bitwise_and}")
print(f"OR bit a bit: {bitwise_or}")
print(f"XOR bit a bit: {bitwise_xor}")
print(f"NOT bit a bit: {bitwise_not}")

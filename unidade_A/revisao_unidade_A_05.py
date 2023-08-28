# Booleanos em Python representam os valores True (Verdadeiro) ou False (Falso).

# Exemplos de comparações:
print(10 > 9)  # True, porque 10 é maior que 9
print(10 == 9)  # False, porque 10 não é igual a 9
print(10 < 9)  # False, porque 10 não é menor que 9

# Exemplos de comparação com condicional:
a = 200
b = 33

if b > a:
    print("b é maior que a")  # Não será impresso, porque b não é maior que a
else:
    print("b não é maior que a")  # Isso será impresso

# O resultado de uma comparação pode ser armazenado em uma variável bool:
resultado = 10 > 9  # resultado é True

# As funções `bool()` podem ser usadas para verificar se um valor é True ou False.
print(bool("Hello"))  # True, porque uma string não vazia é avaliada como True
print(bool(15))  # True, porque um número não zero é avaliado como True

x = "Hello"
y = 15

print(bool(x))  # True, porque a string x não está vazia
print(bool(y))  # True, porque o número y não é zero

# Exemplos de funções que retornam booleanos:

# Função que verifica se um número é par:
def is_par(numero):
    return numero % 2 == 0

print(is_par(4))  # True, porque 4 é par
print(is_par(7))  # False, porque 7 não é par

# Função que verifica se uma string tem mais de 5 caracteres:
def tem_mais_de_cinco_caracteres(texto):
    return len(texto) > 5

print(tem_mais_de_cinco_caracteres("Python"))  # True
print(tem_mais_de_cinco_caracteres("C"))  # False

### Casting em Python
# Casting é a conversão de um tipo de dado para outro tipo de dado.

# Em Python, os tipos de dados mais comuns são:
# Exemplo 1: Casting de inteiros
valor_inteiro = 42
valor_float = float(valor_inteiro)  # Converte o inteiro em um float
print(valor_float)  # Resultado: 42.0

# Exemplo 2: Casting de floats
valor_float = 3.14
valor_inteiro = int(valor_float)  # Converte o float em um inteiro (truncando as casas decimais)
print(valor_inteiro)  # Resultado: 3

# Exemplo 3: Casting de float para string
valor_float = 3.14
valor_str = str(valor_float)  # Converte o float em uma string
print(valor_str)  # Resultado: "3.14"

# Exemplo 4: Casting de string para int
valor_str = "42"
valor_inteiro = int(valor_str)  # Converte a string em um inteiro
print(valor_inteiro)  # Resultado: 42

# Exemplo 5: Casting de string para float
valor_str = "3.14"
valor_float = float(valor_str)  # Converte a string em um float
print(valor_float)  # Resultado: 3.14

# Exemplo 6: Casting de int para string
valor_inteiro = 42
valor_str = str(valor_inteiro)  # Converte o inteiro em uma string
print(valor_str)  # Resultado: "42"

# Exemplo 7: Outros exemplos
x = int(1)       # x será 1
y = int(2.8)     # y será 2
z = int("3")     # z será 3

a = float(1)     # a será 1.0
b = float(2.8)   # b será 2.8
c = float("3")   # c será 3.0
d = float("4.2") # d será 4.2

s1 = str("s1")   # s1 será 's1'
s2 = str(2)      # s2 será '2'
s3 = str(3.0)    # s3 será '3.0'

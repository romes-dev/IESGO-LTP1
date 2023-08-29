# Números em Python

# 1. Números inteiros
# 2. Números de ponto flutuante
# 3. Números complexos

# 1. Números inteiros
# 1.1. Números inteiros positivos
print("Números inteiros positivos")
print(200)
print(1)
print(78272)

# 1.2. Números inteiros negativos
print("Números inteiros negativos")
print(-2)
print(-9)
print(-4223)

# 1.3. Números inteiros positivos e negativos
print("Números inteiros positivos e negativos")
print(0)
print(-0)
print(+0)

# 2. Números de ponto flutuante
# 2.1. Números de ponto flutuante positivos
print("Números de ponto flutuante positivos")
print(1.0)
print(1.1)

# 2.2. Números de ponto flutuante negativos
print("Números de ponto flutuante negativos")
print(-1.0)
print(-1.1)

# 2.3. Números de ponto flutuante positivos e negativos
print("Números de ponto flutuante positivos e negativos")
print(0.0)
print(-0.0)

# 3. Números complexos
# 3.1. Números complexos positivos
print("Números complexos positivos")
print(1 )
print(1j + 1)

# 3.2. Números complexos negativos
print("Números complexos negativos")
print(-1j)
print(-1j - 1)

# 3.3. Números complexos positivos e negativos
print("Números complexos positivos e negativos")
print(0j)
print(-0j)

# Operações com números
# 1. Operações com números inteiros
# 1.1. Operações com números inteiros positivos
print("Operações com números inteiros positivos")
print(1 + 1)
print(1 - 1)

# 1.2. Operações com números inteiros negativos
print("Operações com números inteiros negativos")
print(-1 + -1)
print(-1 - -1)

# 1.3. Operações com números inteiros positivos e negativos
print("Operações com números inteiros positivos e negativos")
print(1 + -1)
print(1 - -1)

# 2. Operações com números de ponto flutuante
# 2.1. Operações com números de ponto flutuante positivos
print("Operações com números de ponto flutuante positivos")
print(1.0 + 1.0)
print(1.0 - 1.0)

# 2.2. Operações com números de ponto flutuante negativos
print("Operações com números de ponto flutuante negativos")
print(-1.0 + -1.0)
print(-1.0 - -1.0)

# 2.3. Operações com números de ponto flutuante positivos e negativos
print("Operações com números de ponto flutuante positivos e negativos")
print(1.0 + -1.0)

# 3. Operações com números complexos
# 3.1. Operações com números complexos positivos
print("Operações com números complexos positivos")
print(1j + 1j)
print(1j - 1j)

# 3.2. Operações com números complexos negativos
print("Operações com números complexos negativos")
print(-1j + -1j)
print(-1j - -1j)

# 3.3. Operações com números complexos positivos e negativos
print("Operações com números complexos positivos e negativos")
print(1j + -1j)
print(1j - -1j)

# 4. Operações com números inteiros e de ponto flutuante
# 4.1. Operações com números inteiros e de ponto flutuante positivos
print("Operações com números inteiros e de ponto flutuante positivos")
print(1 + 1.0)
print(1 - 1.0)

# 4.2. Operações com números inteiros e de ponto flutuante negativos
print("Operações com números inteiros e de ponto flutuante negativos")
print(-1 + -1.0)

# 4.3. Operações com números inteiros e de ponto flutuante positivos e negativos
print("Operações com números inteiros e de ponto flutuante positivos e negativos")
print(1 + -1.0)

#### Exemplos de operações com números inteiros e de ponto flutuante

# Solicitar o preço de vários itens e a quantidade comprada
preco_item1 = float(input("Digite o preço do primeiro item: R$ "))
quantidade_item1 = int(input("Digite a quantidade do primeiro item: "))

preco_item2 = float(input("Digite o preço do segundo item: R$ "))
quantidade_item2 = int(input("Digite a quantidade do segundo item: "))

# Calcular o preço total de cada item
subtotal_item1 = preco_item1 * quantidade_item1
subtotal_item2 = preco_item2 * quantidade_item2

# Calcular o preço total da compra
preco_total = subtotal_item1 + subtotal_item2

# Exibir os totais de cada item e o preço total da compra
print("\nDetalhes da Compra:")
print(f"Item 1: Preço Total = R$ {subtotal_item1:.2f}")
print(f"Item 2: Preço Total = R$ {subtotal_item2:.2f}")
print(f"Preço Total da Compra = R$ {preco_total:.2f}")



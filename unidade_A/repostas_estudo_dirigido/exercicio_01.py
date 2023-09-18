# Exercício 1: Faça uma função que recebe um número e retorna True se ele é múltiplo de 5 ou False caso contrário.

# Operador representado pelo símbolo de porcentagem (%), que retorna o resto da divisão entre dois números. Exemplo: 5 % 2 = 1.

# Um número será múltiplo de 5 se o resto da divisão dele por 5 for igual a 0.

def multiplo_de_5(numero):
    if numero % 5 == 0:
        return True
    else:
        return False

print(multiplo_de_5(int(input("Digite um número: "))))


# Mesmo programa em duas linhas de código:
numero = int(input("Digite um número inteiro: "))
print(f"True" if numero % 5 == 0 else f"False")


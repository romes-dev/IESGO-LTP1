# Entendendo um pouco mais sobre String Methods em Python

# Exemplo 1
def funcao_substituir_texto(texto):
    return texto.replace('Python', 'Java')

print(funcao_substituir_texto('Eu gosto de Python'))

# Exercício 1 - Crie uma função que solicite ao usuário digitar uma palavra e substitua as vogais por "*" e a execute numa aplucação que solicite uma palavra ao usuário e imprima o resultado no console.

def substituir_vogais(texto):
    return texto.replace('a', '*').replace('e', '*').replace('i', '*').replace('o', '*').replace('u', '*')

print(substituir_vogais(input('Digite uma palavra: ')))

# Exemplo 2 - Função que retorna o tamanho de uma string

def tamanho_string(texto):
    return len(texto)

print(tamanho_string('Python'))
texto_user = input('Digite uma palavra: ')
print("Sua palavra tem "+ str(tamanho_string(texto_user)) + " caracteres")

# Exemplo 3 - Usando o método Count
def contar_caracteres(texto):
    return texto.count('a')
print(contar_caracteres('Abelha'))

# Exemplo 4 - Usando o método Capitalize
def capitalizar(texto):
    return texto.capitalize()

print(capitalizar('python'))

# Exemplo 5 - Usando o método Title
def capitalizar_titulo(texto):
    return texto.title()

print(capitalizar_titulo('python é legal'))

# Exemplo 6 - Usando o método Upper
def maiusculas(texto):
    return texto.upper()

# Exemplo 7 - Usando o método Lower
def minusculas(texto):
    return texto.lower()

# Exemplo 8 - Usando o método Swapcase
def inverter_maiusculas_minusculas(texto):
    return texto.swapcase()

# Exemplo 9 - Usando o método Strip
def remover_espacos(texto):
    return texto.strip()

# Exemplo 10 - Usando o método Split
def separar_palavras(texto):
    return texto.split()

# Exemplo 11 - Usando o método Join
def juntar_palavras(texto):
    return ' '.join(texto)

# Exemplo 12 - Usando o método Find
def encontrar_palavra(texto):
    return texto.find('Python')

# Exemplo 13 - Usando o método Startswith
def comeca_com(texto):
    return texto.startswith('Python')


# Praticando um pouco mais


# Solicite ao usuário que insira uma palavra
palavra = input("Digite uma palavra ou frase: ")

# Informações básicas
tamanho = len(palavra)
é_palavra = palavra.isalpha()
é_frase = ' ' in palavra

# Verifique se a palavra contém apenas letras
contém_letras = palavra.isalpha()

# Verifique se a palavra contém apenas dígitos
contém_dígitos = palavra.isdigit()

# Verifique se a palavra está em maiúsculas
em_maiúsculas = palavra.isupper()

# Verifique se a palavra está em minúsculas
em_minúsculas = palavra.islower()

# Apresente as informações ao usuário
print(f"Comprimento da palavra/frase: {tamanho} caracteres")
if é_palavra:
    print("É uma palavra.")
elif é_frase:
    print("É uma frase.")
else:
    print("É uma sequência de caracteres.")
    
if contém_letras:
    print("Contém apenas letras.")
else:
    print("Não contém apenas letras.")
    
if contém_dígitos:
    print("Contém apenas dígitos.")
else:
    print("Não contém apenas dígitos.")
    
if em_maiúsculas:
    print("Está em maiúsculas.")
elif em_minúsculas:
    print("Está em minúsculas.")
else:
    print("Está em uma combinação de maiúsculas e minúsculas.")


# Lista com os 30 métodos de String usados em Python e uma breve descrição de cada um deles
"""
count() - Retorna o número de vezes que uma determinada palavra aparece numa string
casefold() - Retorna uma string em minúsculas
encode() - Retorna uma versão codificada da string
format() - Formata uma string
format_map() - Formata uma string usando um mapeamento
expandtabs() - Define o tamanho do tab
center() - Retorna uma string centralizada
ljust() - Retorna uma string justificada à esquerda
rjust() - Retorna uma string justificada à direita
join() - Junta elementos de uma lista
isalnum() - Retorna True se todos os caracteres da string forem alfanuméricos
isalpha() - Retorna True se todos os caracteres da string forem alfabéticos
decode() - Decodifica a string
diigits() - Retorna uma string contendo apenas dígitos
rfind() - Busca na string por um valor e retorna a última posição em que foi encontrado
rpartition() - Retorna uma tupla onde a string é dividida em três partes
lower() - Converte uma string em minúsculas
upper() - Converte uma string em maiúsculas


"""


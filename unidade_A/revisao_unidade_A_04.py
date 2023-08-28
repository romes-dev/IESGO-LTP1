# Python Strings: Strings são sequências de caracteres em Python, podem ser definidas com aspas simples ou duplas.
string1 = "Olá, mundo!"
string2 = 'Python é divertido.'

# Slicing Strings: Você pode acessar partes de uma string usando índices.
primeira_letra = string1[0]  # Obtém o primeiro caractere (O)
parte_da_string = string2[0:6]  # Obtém os primeiros 6 caracteres (Python)

# Modify Strings: As strings são imutáveis, mas você pode criar uma nova string com as modificações desejadas.
nova_string1 = string1.replace("Olá", "Oi")  # Substitui "Olá" por "Oi"
nova_string2 = string2.upper()  # Converte para letras maiúsculas

# Concatenate Strings: Você pode juntar strings usando o operador de concatenação (+) ou usar f-strings.
nome = "Alice"
saudacao = "Olá, " + nome + "!"
saudacao_fstring = f"Olá, {nome}!"

# Format Strings: Você pode formatar strings usando métodos como format() ou f-strings.
idade = 25
mensagem_format = "Eu tenho {} anos.".format(idade)
mensagem_fstring = f"Eu tenho {idade} anos."

# Escape Characters: Você pode usar caracteres de escape para incluir caracteres especiais em strings.
string_com_escape = "Esta é uma quebra de linha:\nSegunda linha"

# String Methods: Existem muitos métodos disponíveis para manipular strings.
comprimento = len(string1)  # Obtém o comprimento da string
contagem = string2.count("divertido")  # Conta quantas vezes "divertido" aparece

# String Exercises: Exercícios com strings são comuns para praticar Python.
# Aqui está um exemplo simples de trocar maiúsculas por minúsculas e vice-versa.
texto = "ExEmPlo De StrInG"
texto = texto.swapcase()  # Troca maiúsculas por minúsculas e vice-versa

# Imprime os resultados
print(string1)
print(string2)
print(primeira_letra)
print(parte_da_string)
print(nova_string1)
print(nova_string2)
print(saudacao)
print(saudacao_fstring)
print(mensagem_format)
print(mensagem_fstring)
print(string_com_escape)
print(comprimento)
print(contagem)
print(texto)



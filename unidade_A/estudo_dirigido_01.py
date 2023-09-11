# Estudo dirigido de revisão da unidade A. As atividades valem um ponto extra para a prova. Cada exercício deverá ser feito em um arquivo separado, com o nome do arquivo sendo o nome da função. Por exemplo, o exercício 1 deverá ser feito no arquivo multiplo_de_5.py, o exercício 2 deverá ser feito no arquivo multiplo_de_5_e_3.py, e assim por diante.

# Exercício 1: Faça uma função que recebe um número e retorna True se ele é múltiplo de 5 ou False caso contrário.

def multiplo_de_5(numero):
    if numero % 5 == 0:
        return True
    else:
        return False

numero = int(input("Digite um número inteiro: "))

if multiplo_de_5(numero):
    print(f"O número {numero} é múltiplo de 5.")
else:
    print(f"O número {numero} não é múltiplo de 5.")

### Duas linhas de código

numero = int(input("Digite um número inteiro: "))
print(f"O número {numero} é múltiplo de 5." if numero % 5 == 0 else f"O número {numero} não é múltiplo de 5.")

    
# Exercício 2: Faça uma função que recebe um número e imprime no console se ele é múltiplo de 5 e de 3 ou False caso contrário.

def multiplo_de_5_e_3(numero):
    if numero % 5 == 0 and numero % 3 == 0:
        return True
    else:
        return False

numero = int(input("Digite um número inteiro: "))
if multiplo_de_5_e_3(numero):
    print(f"O número {numero} é múltiplo de 5 e de 3.")
else:
    print(multiplo_de_5_e_3(numero))



    

# Exercício 3: Crie um programa em que o usuário insira uma palavra e o programa retorna se a palavra é palíndromo ou não.

# Exercicio 4: Faça um programa que solicita ao usuário escrever o nome das frutas que ele deseja comprar. O usuário deve digitar as frutas até digitar a palavra "sair". O programa deve imprimir na tela a lista de frutas que o usuário deseja comprar.

# Exercício 5: Faça um programa em que o usuário digita o raio de um círculo em m e o programa retorna no console a área do círculo em m² e o perímetro em m.

# Exercício 6: Faça um programa que solicita o ano de nascimento do usuário e retorna o seu signo no horóscopo chinês.

#### Dica: Para descobrir o seu signo no horóscopo chinês, você precisará conhecer o ano do seu nascimento de acordo com o calendário chinês. O horóscopo chinês é baseado em um ciclo de 12 anos, cada ano representado por um animal do zodíaco chinês. Aqui estão os 12 animais do zodíaco chinês e os anos correspondentes:

"""Rato: 2020, 2008, 1996, 1984, 1972, 1960, etc.
Boi (ou Búfalo): 2021, 2009, 1997, 1985, 1973, 1961, etc.
Tigre: 2010, 1998, 1986, 1974, 1962, 1950, etc.
Coelho (ou Gato): 2011, 1999, 1987, 1975, 1963, 1951, etc.
Dragão: 2012, 2000, 1988, 1976, 1964, 1952, etc.
Serpente: 2013, 2001, 1989, 1977, 1965, 1953, etc.
Cavalo: 2014, 2002, 1990, 1978, 1966, 1954, etc.
Cabra (ou Ovelha): 2015, 2003, 1991, 1979, 1967, 1955, etc.
Macaco: 2016, 2004, 1992, 1980, 1968, 1956, etc.
Galo (ou Galinha): 2017, 2005, 1993, 1981, 1969, 1957, etc.
Cão: 2018, 2006, 1994, 1982, 1970, 1958, etc.
Porco: 2019, 2007, 1995, 1983, 1971, 1959, etc.
"""

# Exercício 7: Faça um programa que solicita ao usuário inserir um número inteiro e retorna se ele é primo.

# Exercício 8: Faça um programa que solicita ao usuario inserir um email e retorna se ele é válido ou não.

# Exercício 9: Usando o método random(), crie um programa que solicita ao usuário que adivinhe um número inteiro entre 1 e 10. Se o usuário digitar um número menor que 1 ou maior que 10, solicite que ele insira um número válido. Se o usuário digitar um número válido, verifique se o número que o usuário digitou é igual ao número gerado aleatoriamente pelo programa. Se o número for igual, imprima "Você acertou!". Caso contrário, imprima "Você errou!".

# Exercício 10: Faça um programa que solicita ao usuário escrever um texto e conta quantas vezes a letra "a" aparece no texto.


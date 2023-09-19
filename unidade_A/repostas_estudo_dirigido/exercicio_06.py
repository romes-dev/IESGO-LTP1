
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


def signo_chines(ano):
    signo_chines = ["Rato", "Boi", "Tigre", "Coelho", "Dragão", "Serpente", "Cavalo", "Cabra", "Macaco", "Galo", "Cão", "Porco"]
    calculo = (ano - 1900) % 12
    return signo_chines[calculo]

print(signo_chines(int(input("Digite o ano de nascimento: "))))
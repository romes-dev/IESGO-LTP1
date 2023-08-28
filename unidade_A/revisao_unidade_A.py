# Python Data Types

### Exemplos de tipos de dados em Python
# Confira a tabela abaixo com exemplos dos tipos de dados em Python
"""
+----------------------+-------------------------------------------------+
| Tipo de Dado        | Descrição                                       |
+----------------------+-------------------------------------------------+
| int                  | Números inteiros                               |
| float                | Números de ponto flutuante (decimais)          |
| str                  | Strings (cadeias de caracteres)                |
| bool                 | Valores booleanos (True ou False)              |
| list                 | Listas (coleções mutáveis de elementos)        |
| tuple                | Tuplas (coleções imutáveis de elementos)       |
| dict                 | Dicionários (coleções de pares chave-valor)    |
| set                  | Conjuntos (coleções mutáveis de elementos únicos)|
| frozenset            | Conjuntos imutáveis                            |
| None                 | Valor especial que representa a ausência de valor|
+----------------------+-------------------------------------------------+


"""

# Exemplo 1 - Programa com manipulação de tipos de dados

# Solicitar ao usuário que insira informações
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura em metros: "))
casado = input("Você é casado? (sim/não): ").lower() == "sim"
cores_favoritas = input("Digite suas cores favoritas separadas por vírgula: ").split(",")
comida_preferida = input("Digite sua comida preferida: ")

# Criar um dicionário com as informações
informacoes = {
    "Nome": nome,
    "Idade": idade,
    "Altura": altura,
    "Casado": casado,
    "Cores Favoritas": cores_favoritas,
    "Comida Preferida": comida_preferida
}

# Exibir as informações no console
print("\nInformações do Usuário:")
for chave, valor in informacoes.items():
    print(f"{chave}: {valor}")

# Verificar se o usuário é maior de idade
if idade >= 18:
    print(f"\n{nome} é maior de idade.")
else:
    print(f"\n{nome} não é maior de idade.")

"""

Caso queira aprofundar nos datatypes:

+----------------------+-------------------------------------------------+
| Tipo de Dado        | Categoria                                        |
+----------------------+-------------------------------------------------+
| str                  | Tipo de Texto                                   |
| int                  | Tipos Numéricos (inteiros)                      |
| float                | Tipos Numéricos (números de ponto flutuante)    |
| complex              | Tipos Numéricos (números complexos)             |
| list                 | Tipos de Sequência (listas mutáveis)            |
| tuple                | Tipos de Sequência (tuplas imutáveis)           |
| range                | Tipos de Sequência (intervalos)                 |
| dict                 | Tipo de Mapeamento (dicionários)                |
| set                  | Tipos de Conjunto (conjuntos mutáveis)          |
| frozenset            | Tipos de Conjunto (conjuntos imutáveis)         |
| bool                 | Tipo Booleano                                   |
| bytes                | Tipos Binários (bytes)                          |
| bytearray            | Tipos Binários (bytearrays)                     |
| memoryview           | Tipos Binários (memoryviews)                    |
| NoneType             | Tipo Nenhum (NoneType)                          |
+----------------------+-------------------------------------------------+




Exemplo        | Tipo de Dado    | Teste
---------------|-----------------|------
x = "Hello World" | str             | str
x = 20           | int             | int
x = 20.5         | float           | float
x = 1j           | complexo        | complex
x = ["maçã", "banana", "cereja"] | lista | list
x = ("maçã", "banana", "cereja") | tupla | tuple
x = range(6)     | intervalo       | range
x = {"nome" : "João", "idade" : 36} | dicionário | dict
x = {"maçã", "banana", "cereja"} | conjunto | set
x = frozenset({"maçã", "banana", "cereja"}) | conjunto congelado | frozenset
x = True         | bool            | bool
x = b"Olá"       | bytes           | bytes
x = bytearray(5) | bytearray       | bytearray
x = memoryview(bytes(5)) | visão de memória | memoryview
x = None         | Tipo Nenhum     | NoneType

"""
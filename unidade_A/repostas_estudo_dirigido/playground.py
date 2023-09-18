

# Solicite ao usuário nome e sobrenome e retorne um usuário para login com as três primeiras letras do nome e as três primeiras letras do sobrenome.

# Exemplos de uso de fatiamento de strings em uma tabela:

# | Nome | Sobrenome | Login |
# |------|-----------|-------|
# | João | Silva     | joasil|
# | Maria| Oliveira  | maroli|
# | José | Santos    | jossan|
  
def login():
    nome = input("Digite seu nome: ")
    sobrenome = input("Digite seu sobrenome: ")
    login = nome[:3] + sobrenome[:3]
    print(f"seu login é: {login.lower()}")

login()
    






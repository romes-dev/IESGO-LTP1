import re 
# Exercício 8: Faça um programa que solicita ao usuario inserir um email e retorna se ele é válido ou não.

email_do_usuario = input("Digite seu email: ")

def email_valido(email):
    if "@" in email:    
        return True
    else:
        return False

print(email_valido(email_do_usuario))

# Usando regex:

def checagem_de_email(email):
    padrao = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    resultado = padrao.search(email)
    return resultado != None


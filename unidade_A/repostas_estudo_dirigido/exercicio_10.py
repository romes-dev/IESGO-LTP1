
# Exercício 10: Faça um programa que solicita ao usuário escrever um texto e conta quantas vezes a letra "a" aparece no texto.

texto_exemplo = "Aqui vai um texto arbitrário qualquer com algumas para não dizer várias letras a para contar quantas vezes a letra a aparece alternadamente ou antes ou a posteriori."

def contagem_de_a(texto):
    contagem = 0
    for letra in texto: 
        if letra.lower() == "a":
            contagem += 1
    return contagem

print(texto_exemplo)
print(f"O texto contém a letra 'a' {contagem_de_a(texto_exemplo)} vezes.")

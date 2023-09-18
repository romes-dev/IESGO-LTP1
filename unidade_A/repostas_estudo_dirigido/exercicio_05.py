import math

# Exercício 5: Faça um programa em que o usuário digita o raio de um círculo em m e o programa retorna no console a área do círculo em m² e o perímetro em m.

# Área do cículo = pi * raio²
# Perímetro do círculo = 2 * pi * raio

def area_do_circulo(raio):
    return math.pi * raio ** 2

def perimetro_do_circulo(raio):
    return 2 * math.pi * raio

def dados_do_circulo():
    try:
        raio = float(input("Digite o raio do círculo em m: "))
        print("raio: ", raio)
        print(f"Área do círculo: {area_do_circulo(raio)} m²")
        print(f"Perímetro do círculo: {perimetro_do_circulo(raio)} m")
    except ValueError:
        print("O valor inserido não é um número.")
        dados_do_circulo()
    

dados_do_circulo()
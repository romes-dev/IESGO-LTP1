# File handling (gestão de arquivos)
# Quais são as fun'ões básicas para gestão de arquivo?
### ler (read)
### criar (create)
### escrever (write)
### acrescentar (append)


minha_lista = "/Users/romes/Documents/GitHub/IESGO-LTP1/Unidade_B/minhalista.txt"

f = open(minha_lista)
print(f.readline())
f.close()

numero = 15
for num in range(2, numero):
    print(num)
    if numero % num == 0:
        print("não é primo")
        break
    else:
        print("é primo")

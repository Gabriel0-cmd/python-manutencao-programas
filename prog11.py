def soma_valores(lista):
    total = 0
    for x in lista:
        total += x 
    return total

numeros = []
for i in range(5):
    n = int(input(f"Digite o {i+1}º número: "))
    numeros.append(n)

resultado = soma_valores(numeros)
print("Soma =", resultado)
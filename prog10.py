soma = 0

while True:
    valor = int(input("Digite um valor (0 para sair): "))
    if valor == 0:
        break
    soma += valor

print("Soma =", soma)
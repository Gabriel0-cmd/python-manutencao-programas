valor = int(input("Digite o valor: "))

notas100 = valor // 100
valor %= 100

notas50 = valor // 50
valor %= 50

notas20 = valor // 20
valor %= 20

print(f"{notas100} nota(s) de 100")
print(f"{notas50} nota(s) de 50")
print(f"{notas20} nota(s) de 20")
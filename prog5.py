import random

numero = random.randint(1, 20)  # sorteia de 1 a 20

while True:
    palpite = int(input("Tente adivinhar o número (1 a 20): "))
    if palpite > numero:
        print("Menor")
    elif palpite < numero:
        print("Maior")
    else:
        print("Acertou!")
        break
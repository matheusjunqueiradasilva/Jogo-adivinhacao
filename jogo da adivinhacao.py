import random

rand = random.randint(1, 200)

tentiva = 10

print(" Bem vindo ao jogo da advinhacao!")
print("  Tente advinhar o numero sorteado, e ele deve ser menor que 200!")

while True:

    numero1 = int(input("digite o numero: "))

    if numero1 == rand:
        print(" parabens voce acertou! ")
        break

    elif numero1 > rand:
        print("o numero que chutou foi maior! ")

    elif tentiva == 0:
        break

    else:
        print("o numero chutado foi menor ")

    tentiva -= 1
    print(f" numero restante de tentativas", +tentiva)

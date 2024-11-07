
numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0 and numero != 0:
    print(f"{numero} é PAR.")
elif numero % 2 != 0 or numero == 0:
    print(f"{numero} é ÍMPAR.")
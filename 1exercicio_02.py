
numero = int(input("Digite um número: "))


if numero % 10 == 0:
    print(f"{numero} é divisível por 10.")
elif numero % 5 == 0 or numero % 2 == 0:
    if numero % 5 == 0:
        print(f"{numero} é divisível por 5.")
    if numero % 2 == 0:
        print(f"{numero} é divisível por 2.")
else:
    print(f"{numero} não é divisível por 10, 5 ou 2.")
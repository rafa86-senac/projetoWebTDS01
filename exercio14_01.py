#exercicio 01
contador = 0  # Contador para acompanhar quantos números foram inseridos
negativos = 0  # Contador para números negativos

while contador < 5:  # Enquanto o contador for menor que 5
    numeros = float(input("Digite um número: "))  # Solicita um número
    if numeros < 0:  # Verifica se o número é negativo
       negativos += 1  # Incrementa o contador de negativos
    contador += 1  # Incrementa o contador total

print("Total de números negativos:", negativos)  
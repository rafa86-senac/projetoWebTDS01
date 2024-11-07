
valor_total = float(input("Digite o valor total em reais: "))


num_prestacoes = int(input("Digite o número de prestações desejadas: "))

if num_prestacoes < 12:
    print("O número mínimo de prestações é 12.")
else:

    if num_prestacoes >= 36:
        valor_total *= 1.15  
    elif num_prestacoes >= 24:
        valor_total *= 1.10  

    valor_prestacao = valor_total / num_prestacoes

    print(f"O valor de cada prestação é: R${valor_prestacao:.2f}")

  
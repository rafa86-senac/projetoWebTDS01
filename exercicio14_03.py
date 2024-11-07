# Exercício 03

# Pede ao usuário para informar um número e o converte para inteiro
numero = int(input("Informe um número: "))

# Inicializa a variável i com 1, que será usada para multiplicação
i = 1

# Inicia um loop que continuará enquanto i for menor ou igual a 10
while i <= 10:
    # Calcula o resultado da multiplicação do número pelo valor atual de i
    resultado = numero * i
    
    # Verifica se o resultado é par (divisível por 2)
    if resultado % 2 == 0:
        # Se o resultado for par, imprime a multiplicação formatada
        print(numero, "x", i, "=", resultado)
    
    # Incrementa i em 1 para passar à próxima multiplicação
    i += 1
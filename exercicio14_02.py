# Inicializa os contadores para cada intervalo
contador_0_25 = 0  # Contador para números entre 0 e 25
contador_26_50 = 0  # Contador para números entre 26 e 50
contador_51_75 = 0  # Contador para números entre 51 e 75
contador_76_100 = 0  # Contador para números entre 76 e 100

# Inicializa a variável que irá armazenar o número digitado
numero = 0 

# Inicia um loop que continua enquanto o número for maior ou igual a 0
while numero >= 0:
    # Pede ao usuário para digitar um número
    numero = int(input("Digite um número (negativo para sair): "))
    
    # Verifica em qual intervalo o número se encaixa
    if 0 <= numero <= 25: 
        contador_0_25 += 1  # Incrementa o contador de 0-25
    elif 26 <= numero <= 50:
        contador_26_50 += 1  # Incrementa o contador de 26-50
    elif 51 <= numero <= 75:
        contador_51_75 += 1  # Incrementa o contador de 51-75
    elif 76 <= numero <= 100:
        contador_76_100 += 1  # Incrementa o contador de 76-100

# Imprime os resultados dos contadores
print("Contador 0-25:", contador_0_25) 
print("Contador 26-50:", contador_26_50) 
print("Contador 51-75:", contador_51_75)
print("Contador 76-100:", contador_76_100)
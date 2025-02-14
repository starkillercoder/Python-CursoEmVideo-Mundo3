numeros = []
numeros_pares = []
numeros_impares = []
while True:
    numero = int(input('Digite um número: '))
    numeros.append(numero)
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'A lista completa é {numeros}.')
print(f'A lista de pares é {numeros_pares}.')
print(f'A lista de ímpares é {numeros_impares}.')

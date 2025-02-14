numeros_pares = []
numeros_impares = []
numeros = [numeros_pares, numeros_impares]
for c in range(0, 7):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)
print(f'Números pares: {sorted(numeros[0])}'
      f'\nNúmeros ímpares: {sorted(numeros[1])}')

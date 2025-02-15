numeros = [[], []]
for c in range(1, 8):
    numero = int(input(f'Digite o {c}º valor: '))
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)
print('-=' * 30)
print(f'Os números pares são {sorted(numeros[0])}.')
print(f'Os números ímpares são: {sorted(numeros[1])}')
print('-=' * 30)

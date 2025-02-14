numeros = []
cont = 0
for c in range(0, 5):
    numeros.append(int(input(f'Digite um número na posição {c}: ')))
print(numeros)
print(f'O maior valor é {max(numeros)} nas posições: ', end='')
for v, c in enumerate(numeros):
    if numeros[v] is max(numeros):
        print(f'{v}...', end='')
print(f'\nO menor valor é {min(numeros)} nas posições: ', end='')
for v, c in enumerate(numeros):
    if numeros[v] is min(numeros):
        print(f'{v}...', end='')

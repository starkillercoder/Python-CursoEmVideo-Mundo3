matriz = []
cont = 0
soma_pares = 0
for c in range(0, 3):
    for cc in range(0,3):
        numero = int(input(f'Digite um número para a posição [{c}, {cc}] '))
        matriz.append(numero)
        if numero % 2 == 0:
            soma_pares += numero
print('-=' * 30)
for c in range(0, 9):
    print(f'[{matriz[c]:^5}]', end='')
    if c == 2 or c == 5:
        print()
print(f'\n{'-=' * 30}')
print(f'A soma dos valores pares é {soma_pares}')
print(f'O maior valor da terceira coluna é {(matriz[2] + matriz[5] + matriz[8])}')
print(f'O maior valor da segunda linha é {max(matriz[3:6])}')

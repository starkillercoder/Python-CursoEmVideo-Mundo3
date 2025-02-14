matriz = []
p = 0
c = 0
cont = 0
soma_pares = 0
while True:
    numero = int(input(f'Digite um número para a posição [{p}, {c}] '))
    if numero % 2 == 0:
        soma_pares += numero
    matriz.append(numero)
    c += 1
    if c == 3:
        c = 0
        p += 1
    if p == 3:
        break
print('-=' * 30)
for c in matriz:
    if cont == 3 or cont == 6:
        print(f'\n[ {c} ]', end='')
    else:
        print(f'[ {c} ]', end='')
    cont += 1
print(f'\n{'-=' * 30}')
print(f'A soma dos valores pares é {soma_pares}')
print(f'O maior valor da terceira coluna é {(matriz[2] + matriz[5] + matriz[8])}')
print(f'O maior valor da segunda linha é {max(matriz[3:6])}')

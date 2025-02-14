matriz = []
p = 0
c = 0
cont = 0
while True:
    numero = int(input(f'Digite um número para a posição [{p}, {c}] '))
    matriz.append(numero)
    c += 1
    if c == 3:
        c = 0
        p += 1
    if p == 3:
        break
for c in matriz:
    if cont == 3 or cont == 6:
        print(f'\n[ {c} ]', end='')
    else:
        print(f'[ {c} ]', end='')
    cont += 1

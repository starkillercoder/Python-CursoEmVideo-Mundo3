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
for c in range(0, 9):
    print(f'[{matriz[c]:^5}]', end='')
    if c == 2 or c == 5:
        print()

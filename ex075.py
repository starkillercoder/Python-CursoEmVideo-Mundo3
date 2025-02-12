numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))
numero_3 = int(input('Digite mais um número: '))
numero_4 = int(input('Digite um último número: '))
numeros = (numero_1, numero_2, numero_3, numero_4)
print(f'O número 9 apareceu {numeros.count(9)} vezes.')
print(f'O números 3 apareceu na posição {numeros.count(3)}')
print('Os números pares são:', end= ' ')
for c in range(0, 4):
    if numeros[c] % 2 == 0:
        print(numeros[c],end='')
        if c < 3:
            print(',', end=' ')

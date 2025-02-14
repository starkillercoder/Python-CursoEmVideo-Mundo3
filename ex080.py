numeros = []
for c in range(0, 5):
    numero = int(input('Digite um número: '))
    if c == 0 or numero > numeros[-1]:
        numeros.append(numero)
        print('Adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(numeros):
            if numero <= numeros[pos]:
                numeros.insert(pos, numero)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print(f'Os valores digitados em ordem foram: {numeros}')

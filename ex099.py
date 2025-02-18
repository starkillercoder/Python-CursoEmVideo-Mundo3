from time import sleep
def maior(*n):
    cont = maior = 0
    while True:
        if cont == len(n):
            break
        if cont == 0:
            maior = n[cont]
        else:
            if n[cont] > maior:
                maior = n[cont]
        cont += 1
    print('-=' * 30)
    print(f'Os valores são {n}. Foram digitados {len(n)} valores.')
    print(f'O maior valor entre eles é {maior}')
    sleep(1)


maior(8, 4, 5, 2)
maior(1, 7, 4, 6, 2, 1, 6)
maior(0, 3, 1)
maior(0, 9)
maior()

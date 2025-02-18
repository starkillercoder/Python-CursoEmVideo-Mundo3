from time import sleep
def contagem(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contando de {i} até {f} de {p} em {p}.')
    if i < f:
        while True:
            print(i, end=' ')
            sleep(0.5)
            if i == f:
                break
            i += p
    if i > f:
        while True:
            print(i, end=' ')
            sleep(0.5)
            if i == f:
                break
            i -= p
    print('FIM!')

    
def lin():
    print('-=' * 30)


lin()
contagem(1, 10, 1)
lin()
contagem(20, 10, 2)
lin()
print('Sua vez de personalizar a contagem!')
i = int(input('Início da contagem: '))
f = int(input('Fim da contagem: '))
p = int(int(input('Passo da contagem: ')))
contagem(i, f, p)

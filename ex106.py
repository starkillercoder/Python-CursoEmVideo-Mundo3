from time import sleep
cores = ['\033[m', '\033[40m', '\033[41m', '\033[42m',
         '\33[44m']
def msg(txt, cor=0):
    num = len(txt) + 2
    print(cores[cor], end='')
    print('-' * num)
    print(f' {txt}')
    print('-' * num)
    print(cores[0], end='')
def ajuda(res):
    msg(f'Acessando manual do comando {resposta}', 4)
    sleep(1)
    print(cores[3], end='')
    help(res)
    print(cores[0], end='')
    sleep(1)
while True:
    msg('SISTEMA DE AJUDA PyHELP', 2)
    resposta = str(input('Função ou Biblioteca > '))
    if resposta.upper().strip() == 'FIM':
        break
    ajuda(resposta)
msg('ATÉ LOGO', 2)

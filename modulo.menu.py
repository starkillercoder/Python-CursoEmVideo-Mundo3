def linha(n=42):
    print('-' * n)


def cabecalho(msg):
    linha()
    print(msg.center(42))
    linha()


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'{'\33[31m'}Digite um número inteiro válido.{'\33[m'}')
        except KeyboardInterrupt:
            print(f'{'\33[31m'}O usuário preferiu não informar o valor.{'\33[m'}')
            return 0
        else:
            return n


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    for k, c in enumerate(lista):
        print(f'{k + 1} - {c}')
    linha()
    opc = leiaint('Sua opção: ')
    return opc

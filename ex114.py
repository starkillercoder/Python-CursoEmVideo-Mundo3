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


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f'{'\33[31m'}Digite um número real válido{'\33[m'}.')
        except KeyboardInterrupt:
            print(f'\n{'\33[31m'}O usuário preferiu não informar o valor.{'\33[m'}')
            return 0
        else:
            return n


nint = leiaint('Digite um número inteiro: ')
nflo = leiafloat('Digite um número real: ')
print(f'O valor inteiro informado foi {nint} e o valor real foi {nflo}.')

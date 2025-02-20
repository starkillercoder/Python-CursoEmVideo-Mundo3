def leiaInt(n):
    m = str(input(n)).strip()
    while m.isnumeric()==False:
        print(f'{'\33[31m'}{'ERRO! Digite um número inteiro válido'}{'\33[m'}')
        m = str(input(n)).strip()
    if m.isnumeric():
        return m
a = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {a}')

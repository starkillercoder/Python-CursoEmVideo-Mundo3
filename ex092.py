from datetime import date
ficha = dict()
ficha['Nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
ficha['Idade'] = date.today().year - ano
ficha['CTPS'] = int(input('CTPS: '))
if ficha['CTPS'] != 0:
    ficha['Salário'] = float(input('Salário: '))
    ficha['Contratação'] = int(input('Ano de contratação: '))
    ficha['Aposentadoria'] = (ficha['Contratação'] - ano) + 35
    print('-' * 30)
    for i, v in ficha.items():
        print(f'{i}: {v}')
    print('-' * 30)
if ficha['CTPS'] == 0:
    print('-' * 30)
    for i, v in ficha.items():
        print(f'{i}: {v}')
    print('-' * 30)

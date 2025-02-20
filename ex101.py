from datetime import date
def voto(ano):
    idade = date.today().year - ano
    if 18 <= idade <= 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    elif idade < 16:
        return f'Com {idade} anos: VOTO NEGADO.'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL.'
n = int(input('Ano de nascimento: '))
print(voto(n))

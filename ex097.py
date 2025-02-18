def msg(txt):
    num = len(txt) + 2
    print('-' * num)
    print(f'{txt:^{num}}')
    print('-' * num)

msg('Diego')
msg('Eu amo o Twice')
msg('Up no more')

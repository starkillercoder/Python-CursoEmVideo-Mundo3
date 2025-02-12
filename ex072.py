por_extenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis",
               "sete", "oito", "nove", "dez", "onze", "doze", "treze",
               "quatorze", "quinze", "dezesseis", "dezessete", "dezoito",
               "dezenove", "vinte")
numero = int(input('Digite um número: '))
numerico = por_extenso[numero]
print(f'Você digitou o número {numerico}')

'''Determine se um determinado ano lido e bissexto. Sendo que um ano e 
bissexto se for divisıvel por 400 ou se for divisıvel por 4 e nao for divisıvel 
por 100. Por exemplo: 1988, 1992, 1996'''

ano = input('Digite o ano: ')
try:
    ano = int(ano)
    if ano >= 0:
        if ano % 4 == 0 or ano % 400 == 0 and ano % 100 != 0:
            print(f'{ano} é um ano bissexto')
        else:
            print(f'{ano} não é um ano bissexto.')
    else:
        print('Ano inválido.')
except:
    print('Apenas valores numéricos positivos são permitidos;')
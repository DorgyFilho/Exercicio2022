'''Tendo como dado de entrada a altura (h) de uma pessoa, construa um 
algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7'''

sexo = input('Digite o sexo (M ou F): ').upper()
if sexo not in ('M','F'):
    print('Informação inválida.')
else:
    h = input('Digite a altura em m: ')
    try:
        h = float(h)
        if h > 0 and sexo == 'M':
            pesoH = (72.7*h) - 58
            print(f'O peso ideal do homem é: {pesoH:.2f} kg')
        elif h > 0 and sexo == 'F':
            pesoM = (62.1*h) - 44.7
            print(f'O peso ideal da mulher é: {pesoM:.2f} kg')
    except:
        print('Informação inválida')
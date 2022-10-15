'''Fac¸a um programa para verificar se um determinado numero inteiro e 
divisıvel por 3 ou 5, mas nao simultaneamente pelos dois. '''

num = input('Digite um número: ')
try:
    num = int(num)
    if (num % 3 == 0 and num % 5 == 0):
        print(f'{num} é divisível por 3 e por 5. Número não permitido.')
    else:
        print(f'{num} é um número permitido, pois ele é divisível por 3 ou por 5.')
except:
    print('Apenas valores numéricos são permitidos.')

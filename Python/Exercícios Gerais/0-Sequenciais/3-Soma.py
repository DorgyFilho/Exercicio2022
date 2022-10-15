'''Faça um Programa que peça dois números e imprima a soma.'''

a = input('Digite um número: ')
try:
    a = int(a)
    b = input('Digite outro número: ')
    try:
        b = int(b)
        soma = a + b
        print(f'A soma é {soma}')
    except:
        print('Informação inválida')

except:
    print('Informação invalida.')    

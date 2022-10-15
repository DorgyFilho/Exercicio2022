'''Tabela de Multiplicação'''

a = input('Digite o número a: ')
try:
    a = int(a)
    b = input('Digite o número b: ')
    try:
        b = int(b)
        for i in range(1, b+1):
            result = a * i
            print(f'{a} x {i} = {result}')
    except:
        print('Número b é inválido')
except:
    print('Número a é inválido.')
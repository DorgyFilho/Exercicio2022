'''Leia um numero real. Se o numero for positivo imprima a raiz quadrada. 
Do contrario, imprima o numero ao quadrado'''

from math import sqrt

num = input('Digite um número: ')
try:
    num = int(num)
    if num >= 0:
        raiz = sqrt(num)
        print(f'A raíz de {num} é {raiz:.1f}')
    else:
        quadrado = num**2
        print(f'O quadrado de {num} é {quadrado}')
except:
    print('Apenas valores numéricos são válidos.')
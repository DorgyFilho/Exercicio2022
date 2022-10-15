'''Leia um numero fornecido pelo usuario. Se esse numero for positivo, 
calcule a raiz quadrada do numero. Se o numero for negativo, mostre uma 
mensagem dizendo que o numero e invalido. '''

from math import sqrt

num = input("Digite o número: ")
try:
    num = int(num)
    if num > 0:
        raiz = sqrt(num)
        print(f'A raíz de {num} é {raiz:.1f}')
    else:
        print('Não existe raíz de numero negativo.')
except:
    print('Apenas valores numéricos são válidos.')
'''Faca um programa que leia um numero e, caso ele seja positivo, calcule e 
mostre: 
• O numero digitado ao quadrado
• A raiz quadrada do numero digitado'''

from math import sqrt

num = input('Digite um número: ')
try:
    num = int(num)
    if num >= 0:
        quadrado = num**2
        raiz = sqrt(num)
        print(f'O quadrado de {num} é {quadrado}\nA raiz quadrada de {num} é {raiz}')
    else:
        print('Número negativo.')
except:
    print('Informação inválida.')

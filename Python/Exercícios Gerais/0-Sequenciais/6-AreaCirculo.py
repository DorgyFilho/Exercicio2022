'''Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.'''

r = input('Digite o raio do círculo: ')
try:
    r = int(r)
    pi = 3.14
    area = pi*(r**2)
    print(f'A área do círculo é {area}')
except:
    print('Informação inválida.')
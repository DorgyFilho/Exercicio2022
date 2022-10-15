'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.'''

n1 = int(input('Número 1: '))
n2 = int(input("Número 2: "))
n3 = float(input('Número 3: '))

calculo1 = (n1*2)*(n2/2)
calculo2 = (n1*3) + n3
calculo3 = (n3**2)

print(f'Resposta 1: {calculo1}\nResposta 2: {calculo2}\nResposta 3: {calculo3}')
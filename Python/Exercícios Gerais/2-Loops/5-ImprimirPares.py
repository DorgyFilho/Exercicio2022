'''Faça um programa que imprima apenas os números pares de uma sequência'''

num = input('Digite um número: ')
try: 
    num = int(num)
    for i in range(1, num+1):
        if i % 2 == 0:
            print(i)
except:
    print('Apenas valores numéricos são válidos')
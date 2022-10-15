'''Imprimir até enésima linha'''

def nLinha(num):
    for i in range(1, num+1):
        for j in range(1, i+1):
            print(i, end=' ')
        print()

num = input('Digite um numero: ')
try:
    num = int(num)
    nLinha(num)
except:
    print('Informação Inválida')
'''Imprimir até enésima linha 2'''

def nLinha(num):
    for i in range(1, num+1):
        for j in range(1, i+1):
            print(j, end=' ')
        print()

num = input('Digite um número: ')
try:
    num = int(num)
    nLinha(num)
except:
    print('Informação inválida.')
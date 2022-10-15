'''Positivo ou negativo'''

def PosNeg(num):
    if num > 0:
        return 'Positivo'
    else:
        return 'Negativo'

num = input('Digite um número: ')
try:
    num = int(num)
    print(PosNeg(num))
except:
    print('Informação inválida.')
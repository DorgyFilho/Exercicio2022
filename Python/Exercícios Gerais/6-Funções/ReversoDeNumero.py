'''Reverso de um número'''

def ReversoNum(num):
    Num = str(num)
    NumInv = Num[::-1]
    return f'{Num} -> {NumInv}'

num = input('Digite um número: ')
try:
    num = int(num)
    print(ReversoNum(num))
except:
    print('Informação inválida.')
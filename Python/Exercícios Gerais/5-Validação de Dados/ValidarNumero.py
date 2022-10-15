'''Validar Número'''

num = input('Digite um número: ')
try:
    num = int(num)
    print('Informação válida')
except:
    print('Informação inválida.')
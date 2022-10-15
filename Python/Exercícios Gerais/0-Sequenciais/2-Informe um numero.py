'''Faça um Programa que peça um número e então 
mostre a mensagem O número informado foi [número].'''

num = input('Informe um número: ')
try:
    num = int(num)
    print(f'O número informado foi {num}')
except:
    print('Informação inválida')
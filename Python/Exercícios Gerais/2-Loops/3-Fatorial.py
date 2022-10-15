'''Faça um programa que calcule o fatorial de um número inteiro fornecido 
pelo usuário. Ex.: 5!=5.4.3.2.1=120'''

def Fatorial(num):
    fat = 1
    valor = num
    print(f'{valor}! = ', end=' ')
    while valor > 0:
        print(f'{valor}', end=' ')
        print('.' if valor > 1 else '=', end=' ')
        fat *= valor
        valor -= 1
    print(f'{fat}', end=' ')

def Main():

    while True:
        print()
        num = input('Digite um número: ')
        if num == '':
            print('Programa encerrado.')
            break
        else:
            try:
                num = int(num)
                if num < 0:
                    print('Apenas valores positivos são aceitos.')
                else:
                    Fatorial(num)
            except:
                print('Apenas valores numéricos são permitidos.')
Main()

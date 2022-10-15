'''Faça um programa que receba dois números inteiros e gere os números inteiros 
que estão no intervalo compreendido por eles.'''

num = input('Digite um número: ')
try:
    num = int(num)
    num2 = input('Digite outro número: ')
    try:
        num2 = int(num2)
        while num2 < num:
            num = input('Digite um número: ')
            try:
                num = int(num)
                num2 = input('Digite outro número: ')
                try:
                    num2 = int(num2)
                except:
                    print('Inválido.')
            except:
                print('Inválido')
        else:
            for i in range(num+1, num2):
                print(i, end=' ')
    except:
        print('Inválido.') 
except:
    print('Inválido.')                       
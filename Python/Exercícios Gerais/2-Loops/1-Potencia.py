'''Faça um programa que peça dois números, base e expoente, calcule e mostre 
o primeiro número elevado ao segundo número. Não utilize a função de potência 
da linguagem.'''

a = input('Digite a base: ')
try: 
    a = int(a)
    b = input('Digite o expoente: ')
    try:
        b = int(b)
        for i in range(b+1):
            calculo = a ** i
        print(f'{a}^{i} = {calculo}')
    except:
        print('Apenas valores numéricos são aceitos.')
except:
    print('Apenas valores numéricos são aceitos.')

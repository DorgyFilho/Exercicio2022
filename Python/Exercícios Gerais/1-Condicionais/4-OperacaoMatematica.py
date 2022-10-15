'''Faca um programa que mostre ao usuario um menu com 4 opcoes de operacoes 
matematicas (as basicas, por exemplo). O usuario escolhe uma das opcoes e o seu 
programa entao pede dois valores numericos e realiza a operacao, mostrando o 
resultado e saindo.'''

def Soma(a,b):
    return f'Resultado: {a + b}'

def Subtracao(a,b):
    return f'Resultado: {a - b}'

def Multiplicacao(a,b):
    return f'Resultado: {a * b}'

def Divisao(a,b):
    return f'Resultado: {a / b}'

def Main():

    while True:
        print('1-Somar\n2-Subtrair\n3-Multiplicar\n4-Dividir\n5-Sair\nEscolha uma opcao acima')
        resposta = input('Digite a sua escolha: ')
        if resposta == '1':
            a = input('Número a: ')
            try:
                a = int(a)
                b = input('Número b: ')
                try:
                    b = int(b)
                    print()
                    print(Soma(a,b))
                    print()
                except:
                    print()
                    print('Valor inválido')
                    print()
            except:
                print()
                print('Valor Inválido')
                print()

        elif resposta == '2':
            a = input('Número a: ')
            try:
                a = int(a)
                b = input('Número b: ')
                try:
                    b = int(b)
                    print()
                    print(Subtracao(a,b))
                    print()
                except:
                    print()
                    print('Valor invalido.')
                    print()
            except:
                print()
                print('Valor Inválido')
                print()
        
        elif resposta == '3':
            a = input('Número a: ')
            try:
                a = int(a)
                b = input('Número b: ')
                try:
                    b = int(b)
                    print()
                    print(Multiplicacao(a,b))
                    print()
                except:
                    print()
                    print('Valor inválido.')
                    print()
            except:
                print()
                print('Valor inválido.')
                print()
        
        elif resposta == '4':
            a = input('Número a: ')
            try:
                a = int(a)
                b = input('Número b: ')
                try:
                    b = int(b)
                    print()
                    print(Divisao(a,b))
                    print()
                except:
                    print()
                    print('Valor inválido.')
                    print()
            except:
                print()
                print('Valor inválido.')
                print()

        elif resposta == '5':
            print('Programa encerrado.')
            break
        else:
            print()
            print('Opção inválida. Tente novamente.')
            print()

Main()                
'''Fatorial'''

def Fatorial(num):
    if num < 0:
        return 'Fatorial de Número Negativo Não Existe'
    elif num == 0:
        return f'O fatorial de {num} é 1'
    else:
        fat = 1
        valor = num
        while valor > 1:
            fat *= valor
            valor -= 1
        return f'O fatorial de {num} é {fat}'

def main():
    while True:
        num = input('Digite um número: ').upper()
        if num == 'N':
            print('Programa encerrado.')
            break
        else:
            try:
                num = int(num)
                print(Fatorial(num))
            except:
                print('Informação inválida')

main()
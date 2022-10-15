'''Tabela de Preços - Padaria'''

PrecoUnitPao = 0.20

QtdPaes = input('Digite a quantidade de pães: ')
try:
    QtdPaes = int(QtdPaes)
    for i in range(1, QtdPaes+1):
        Valor = i * PrecoUnitPao
        print(f'{i} Pão(es) - R${Valor:.2f}')
except:
    print('Informação inválida.')
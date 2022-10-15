'''Faça um programa que calcule o valor total investido por um colecionador 
em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá 
informar a quantidade de CDs e o valor para em cada um.'''

qtd = input('Digite a quantidade de cds: ')
mediaPreco = 0
totalPreco = 0
try:
    qtd = int(qtd)
    for i in range(1, qtd+1):
        preco = input(f'Digite o valor do {i}° CD: ')
        try:
            preco = float(preco)
            totalPreco += preco
        except:
            totalPreco = 0
            print('Apenas valores numéricos são aceitos.')
            break
except:
    print('Apenas valores numéricos são aceitos.')

mediaPreco = totalPreco/qtd

print(f'O valor médio gasto em cada CD foi R${mediaPreco:.2f}')
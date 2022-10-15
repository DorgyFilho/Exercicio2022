'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho 
em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é 
de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 
litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta 
a serem compradas e o preço total.'''

metros = input('Digite a quantidade de metros: ')

try:
    metros = float(metros)
    Litros = metros/3
    PrecoLata = 80
    QtdLtsPorLata = 18

    LatasCompradas = Litros / QtdLtsPorLata
    ValorTotal = LatasCompradas*PrecoLata 

    print(f'Qtd Latas a Serem Compradas: {LatasCompradas:.2f} Litros \
        \nValor total da compra: R${ValorTotal:.2f}')

except:
    print('Apenas valores numéricos são aceitos.')
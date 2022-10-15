'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho 
em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é 
de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 
litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos 
preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. 
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, 
considere latas cheias.'''

metros = input('Digite a quantidade de metros: ')

try:
    metros = float(metros)
    Litros = metros/6
    QtdTintaLata = 18
    PrecoLata = 80
    PrecoGalao = 25
    Latas = Litros/18
    Galoes = Litros/3.6

    if metros < 18: #Cai no fato de que a quantidade de metros é inferior à cobertura de 1 litro de tinta
        print('Não pode comprar latas de tinta')
        print(f'Comprando galões, você gastará R${round(Galoes)*PrecoGalao:.2f}')
    else:
        ValorLata = round(Latas)*PrecoLata
        ValorGalao = round(Galoes)*PrecoGalao
        print(f'Comprando lata, você gastará R$ {ValorLata:.2f} \
        \nComprando galões, você gastará R${ValorGalao:.2f}')
except:
    print('Apenas valores numéricos são aceitos')

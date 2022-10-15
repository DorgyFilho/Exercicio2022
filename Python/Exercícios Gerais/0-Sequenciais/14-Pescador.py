'''João Papo-de-Pescador, homem de bem, comprou um microcomputador para 
controlar o rendimento diário de seu trabalho. Toda vez que ele traz um 
peso de peixes maior que o estabelecido pelo regulamento de pesca do estado 
de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos 
além do limite e na variável multa o valor da multa que João deverá pagar. 
Imprima os dados do programa com as mensagens adequadas.'''

peso = input('Digite o peso da carga de peixe: ')
try:
    pesoExcedente = 0
    peso = float(peso)
    if peso > 50:
        pesoExcedente = peso - 50
        valorExcedente = pesoExcedente * 4.00
        ValorTotal = valorExcedente
        print(f'O valor da multa a ser pago é R${ValorTotal:.2f}')
    else:
        ValorTotal = 0
        print('Você não precisa pagar multa.')
except:
    print('Informação inválida.')
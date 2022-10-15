'''Faça um Programa que converta metros para centímetros.'''

metro = input('Digite a quantidade de metro: ')
try:
    metro = int(metro)
    centimetro = metro*100
    print(f'{metro} metro(s) possui(em) {centimetro} centímetro(s)')
except:
    print('Informação inválida.')
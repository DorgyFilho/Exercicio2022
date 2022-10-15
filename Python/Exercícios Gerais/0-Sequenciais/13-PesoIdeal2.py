'''Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo 
que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58'''

h = input('Digite a altura: ')
try:
    h = float(h)
    Peso_Ideal = (72.7*h) - 58
    print('O seu peso ideal é {:.2f} kg'.format(Peso_Ideal))
except:
    print('Apenas números são válidos')
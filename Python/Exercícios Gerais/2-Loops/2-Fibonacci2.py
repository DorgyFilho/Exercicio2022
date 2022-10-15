'''A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
Faça um programa capaz de gerar a série até o n−ésimo termo.'''

num = input('Digite um número: ')
ultimo = 1
penultimo = 1
try:
    num = int(num)
    for i in range(0, num):
        numero = ultimo + penultimo
        penultimo = ultimo
        ultimo = numero
        print(f'{ultimo}', end=' ')
except:
    print('Apenas valores numéricos são permitidos.')
'''Crie uma variável chamada contador = 0. Enquanto counter for menor que 100, 
imprima os valores na tela,mas quando for encontrado o valor 23, 
interrompa a execução do programa.'''

contador = 0
while contador < 100:
    if contador == 23:
        print('Programa encerrado.')
        break
    else:
        print(contador)
        contador += 1
'''Palíndromo'''

frase = input('Escreva uma frase: ').upper() #Deixar tudo em letra maiúscula.
JuntaFrase = frase.replace(' ', '') #Remover os espaços da frase por meio de substituição
FraseInv = JuntaFrase[::-1]
if FraseInv == JuntaFrase:
    print(f'{FraseInv} = {JuntaFrase}')
else:
    print('As frases não são palíndromo')
#Comparar tamanhos entre strings

string1 = input('Escreva uma frase: ')
string2 = input('Escreva outra frase: ')
if len(string1) > len(string2):
    print(f'{string1}: {len(string1)} caracteres')
    print(f'{string2}: {len(string2)} caracteres')
elif len(string2) > len(string1):
    print(f'{string1}: {len(string1)} caracteres\n{string2}: {len(string2)} caracteres')
else:
    print('As strings possuem o mesmo tamanho.')
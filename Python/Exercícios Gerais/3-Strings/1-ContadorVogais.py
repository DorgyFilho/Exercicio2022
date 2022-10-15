'''Conta espaços e vogais. Dado uma string com uma frase informada pelo 
usuário (incluindo espaços em branco), conte:

1.quantos espaços em branco existem na frase.
2.quantas vezes aparecem as vogais a, e, i, o, u.'''

def ContadorEspVog(frase):

    ContadorA = frase.count('a')
    ContadorE = frase.count('e')
    ContadorI = frase.count('i')
    ContadorO = frase.count('o')
    ContadorU = frase.count('u')
    ContEsp = frase.count(' ')
    print(f'a: {ContadorA}\ne: {ContadorE}\ni: {ContadorI}\no: {ContadorO}\nu: {ContadorU}\nEspaço: {ContEsp}')

def main():

    while True:
        frase = input('Digite uma frase: ').lower()
        if frase == '':
            print('Programa encerrado.')
            break
        else:
            ContadorEspVog(frase)

main()
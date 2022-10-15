'''Escreva uma palavra que substitua a palavra "bola" da frase 'Hoje eu vou
jogar bola'''

frase = 'Hoje eu vou jogar bola'
Palavra = input('Digite uma palavra: ').lower()
NovaFrase = frase.replace('bola', Palavra)
print(NovaFrase)
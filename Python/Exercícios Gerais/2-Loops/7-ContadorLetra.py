'''Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. 
Use uma variável contadora na sua instrução de impressão

# “É melhor, muito melhor, contentar-se com a realidade; se ela não é tão 
# brilhante como os sonhos, tem pelo menos a vantagem de existir.” 
# (Machado de Assis'''

def ContaLetraR(frase):
    contador = 0
    for letra in frase:
        if letra == 'r':
            contador += 1
    print(f"Há {contador} r's na frase digitada")

def Main():

    while True:
        frase = input('Digite uma frase: ')
        if frase == '':
            print('Programa encerrado.')
            break
        else:
            ContaLetraR(frase)

Main()
        

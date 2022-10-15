'''Crie uma rotina que recebe como argumento uma String (contendo uma
palavra ou frase) e devolve o conteúdo dessa String sem espaços (se
existirem). Por exemplo, se o argumento recebido for " Universidade
Federal Rural de Pernambuco ", a rotina deverá devolver
“UniversidadeFederalRuraldePernambuco".'''

Frase = input('Digite uma frase: ')
NovaFrase = Frase.replace(' ', '')
print(f'{Frase} ---> {NovaFrase}')
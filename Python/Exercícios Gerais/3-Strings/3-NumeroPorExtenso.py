'''Número por extenso. Escreva um programa que solicite ao usuário 
a digitação de um número até 99 e imprima-o na tela por extenso.'''

def NumExtenso(num):

    dezena = ['vinte','trinta','quarenta','cinquenta',
    'sessenta','setenta','oitenta','noventa']

    unidade = ['zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis',
    'dezessete','dezoito','dezenove']

    try:
        num = int(num)
        if 0 <= num <= 9:
            NumExt = unidade[num]
            print(f'O número digitado é {NumExt}')

        if 10 <= num <= 19:
            NumExt = unidade[num]
            print(f'O número digitado foi {NumExt}')

        if num == 20:
            dez = 0
            NumExt = dezena[dez]
            print(f'O número digitado foi {NumExt}')
        
        else:
            if 20 < num <= 29:
                num = str(num)
                dez = 0
                unid = int(num[1])
                NumExt = dezena[dez] + ' e ' + unidade[unid]
                print(f'O número digitado foi {NumExt}')

        if num == 30:
            dez = 1
            NumExt = dezena[dez]
            print(f'O número digitado foi {NumExt}')

        else:
            if 30 < num <= 39:
                num = str(num)
                dez = 1
                unid = int(num[1])
                NumExt = dezena[dez] + ' e ' + unidade[unid]
                print(f'O número digitado foi {NumExt}')

        if num == 40:
            dez = 2
            NumExt = dezena[dez]
            print(f'O número digitado foi {NumExt}')

        else:
            if 40 < num <= 49:
                num = str(num)
                dez = 2
                unid = int(num[1])
                NumExt = dezena[dez] + ' e ' + unidade[unid]
                print(f'O número digitado foi {NumExt}')
        
        if num == 50:
            dez = 3
            NumExt = dezena[dez]
            print(f'O número digitado foi {NumExt}')
        
        else:
            if 50 < num <= 59:
                num = str(num)
                dez = 3
                unid = int(num[1])
                NumExt = dezena[dez] + ' e ' + unidade[unid]
                print(f'O número digitado foi {NumExt}')

        if num == 60:
            dez = 4
            NumExt = dezena[dez]
            print(f'O número digitado foi {NumExt}')
        
        else:
            if 60 < num <= 69:
                num = str(num)
                dez = 4
                unid = int(num[1])
                NumExt = dezena[dez] + ' e ' + unidade[unid]
                print(f'O número digitado foi {NumExt}')
        
        if num == 70:
            dez = 5
            NumExt = dezena[dez]
            print(f'O número digitado foi {NumExt}')
        
        else:
            if 70 < num <= 79:
                num = str(num)
                dez = 5
                unid = int(num[1])
                NumExt = dezena[dez] + ' e ' + unidade[unid]
                print(f'O número digitado foi {NumExt}')

        if num == 80:
            dez = 6
            NumExt = dezena[dez]
            print(f'O número digitado foi {NumExt}')
        
        else:
            if 80 < num <= 89:
                num = str(num)
                dez = 6
                unid = int(num[1])
                NumExt = dezena[dez] + ' e ' + unidade[unid]
                print(f'O número digitado foi {NumExt}')
            
        if num == 90:
            dez = 7
            NumExt = dezena[dez]
            print(f'O número digitado foi {NumExt}')
        
        else:
            if 90 < num <= 99:
                num = str(num)
                dez = 7
                unid = int(num[1])
                NumExt = dezena[dez] + ' e ' + unidade[unid]
                print(f'O número digitado foi {NumExt}')
        
        if num > 99:
            print('Apenas números de 0 a 99 são permitios.')      
                
    except:
        print('Apenas números são permitidos.')

def main():

    while True:
        num = input('Digite um número: ')
        if num == '':
            print('Programa encerrado.')
            break
        else:
            NumExtenso(num)

main()
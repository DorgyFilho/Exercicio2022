'''. Fac¸a um programa que leia 2 notas de um aluno, verifique se as notas sao 
validas e exiba na tela a media destas notas. Uma nota valida deve ser, 
obrigatoriamente, um valor entre 0.0 e 10.0, onde caso a nota nao possua um 
valor valido, este fato deve ser informado ao usuario e o programa termina.'''

soma = 0
media = 0
for i in range(2):
    nota = input('Digite a nota: ')
    try:
        nota = float(nota)
        if 0.0 <= nota <= 10.0:
            soma += nota
        else:
            media = 0
            soma = 0
            print('Valor inválido.')
            break
    except:
        print('Apenas valores numéricos são válidos.')
        break

media = soma/2

print(f'A média é {media:.2f}')

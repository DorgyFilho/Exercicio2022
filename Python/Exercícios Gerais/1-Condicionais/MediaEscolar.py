nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
soma = nota1 + nota2
media = soma/2

if media == 10.0:
    print('Aprovado com louvor!')
elif 7.0 <= media < 10.0:
    print('Aprovado')
else:
    print('Reprovado')

    
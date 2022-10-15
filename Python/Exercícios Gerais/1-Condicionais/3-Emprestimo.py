'''Leia o salario de um trabalhador e o valor da prestacao de um emprestimo. 
Se a prestacao for maior que 20% do salario imprima: Emprestimo n~ao concedido, 
caso contrario imprima: Emprestimo concedido.'''

salario = input('Escreva seu salário: ')
try:
    salario = float(salario)
    prestacao = input('Valor da prestação a ser pago: ')
    try:
        prestacao = float(prestacao)
        valorPercentual = 0.20*salario
        if prestacao > valorPercentual:
            print('Empréstimo não concedido.')
        else:
            print('Empréstimo concedido')
    except:
        print('Valor inválido.')
except:
    print('Valor inválido.')
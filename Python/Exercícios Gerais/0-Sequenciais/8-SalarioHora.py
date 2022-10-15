'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês.'''

salario = float(input('Salario: '))
salarioDia = salario/30
salarioHora = salarioDia/8
print(f'Salário Hora: R${salarioHora:.2f}')
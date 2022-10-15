'''Faça um Programa que pergunte quanto você ganha por hora e o número de 
horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido 
mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS 
e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.'''

Salario = input('Digite o salario mensal: ')
try:
    Salario = float(Salario)
    SalarioDia = Salario/30
    SalarioHora = SalarioDia/8
    ImpostoRenda = 0.11*Salario
    Inss = 0.08*Salario
    Sindicato = 0.05*Salario
    SalarioLiquido = Salario - ImpostoRenda - Inss - Sindicato
    print(f'Salário Bruto: R${Salario:.2f} \
        \n-INSS: R${Inss:.2f} \
        \n-Sindicato: R${Sindicato:.2f} \
        \n-IR: R${ImpostoRenda:.2f} \
        \n=Salário Líquido: R${SalarioLiquido:.2f}')
except:
    print('Apenas valores numéricos são aceitos.')

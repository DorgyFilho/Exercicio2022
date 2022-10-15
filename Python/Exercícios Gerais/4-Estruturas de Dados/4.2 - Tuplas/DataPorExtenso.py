'''Data Por Extenso'''

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
    'Outubro', 'Novembro', 'Dezembro')
data = input('Digite a data de nascimento no formato DD/MM/AAAA: ').split('/')
dia = int(data[0])
mes = int(data[1])
ano = int(data[2])
if 1 <=  mes <= 12 and 1 <= dia <= 31:
    print(f'Você nasceu no dia {dia} de {meses[mes-1]} de {ano}')
else:
    print('Data inválida')


cent = 0
dez = 0
unid = 0
numero = input('Número: ')
if int(numero) > 100:
    cent = int(numero[0])
    dez = int(numero[1])
    unid = int(numero[2])
    print(f'{cent} centena(s), {dez} dezena(s) e {unid} unidades')
else:
    cent = 0
    dez = int(numero[0])
    unid = int(numero[1])
    print(f'{cent} centena(s), {dez} dezena(s) e {unid} unidades')

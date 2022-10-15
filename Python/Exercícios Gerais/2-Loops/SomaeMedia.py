#Soma e média
from statistics import mean

ListaNumeros = []

for i in range(1,6):
    num = int(input(f'{i}° Número: '))
    ListaNumeros.append(num)

SomaNumeros = sum(ListaNumeros)
MediaNumeros = mean(ListaNumeros)

print(f'A soma dos números é {SomaNumeros}')
print(f'A média é {MediaNumeros}')
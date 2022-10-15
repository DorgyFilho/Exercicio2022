'''Faça um programa que receba tres números e mostre-os em ordem crescente'''

ListaNum = []
for i in range(1,4):
    num = input(f'Digite o {i}° número: ')
    try:
        num = int(num)
        ListaNum.append(num)
    except:
        print('Apenas valores numéricos são permitidos.')
        break

ListaNum.sort()

for i in ListaNum:
    print(i, end=" ")
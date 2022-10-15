'''Pares e Impares'''
Pares = list()
Impares = list()

for i in range(1,21):
    if i % 2 == 0:
        Pares.append(i)
    else:
        Impares.append(i)

print(f'Números Pares: {Pares}')
print(f'Números Impares: {Impares}')

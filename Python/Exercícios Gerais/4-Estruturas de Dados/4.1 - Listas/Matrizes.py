'''Matriz'''
lin = int(input('Linhas: '))
col = int(input('Colunas: '))

Matriz = []
for i in range(1, lin+1):
    aux = []
    for j in range(1, col+1):
        par = int(input(f'({i},{j}: '))
        aux.append(par)
    Matriz.append(aux)

for a in Matriz:
    for b in a:
        print(b, end=' ')
    print()

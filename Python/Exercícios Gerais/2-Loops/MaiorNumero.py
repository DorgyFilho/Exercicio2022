maiorNumero = 0
for i in range(1,6):
    num = int(input(f'{i}° Número: '))
    if num > maiorNumero:
        maiorNumero = num

print(f'O maior número digitado é {maiorNumero}')

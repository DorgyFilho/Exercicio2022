maisBarato = 99999999999
for i in range(1,4):
    preco = float(input(f'Preço {i}: '))
    if preco < maisBarato:
        maisBarato = preco

print(f'Preço mais barato: R${maisBarato}')

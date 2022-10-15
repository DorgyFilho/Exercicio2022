'''Faça um Programa que calcule a área de um quadrado, 
em seguida mostre o dobro desta área para o usuário.'''

l = input('Digite o número que representa o lado: ')
try:
    l = int(l)
    area = l**2
    DobroArea = area*2
    print(f'O dobro da área {area} é {DobroArea}')
except:
    print('Informação inválida.')
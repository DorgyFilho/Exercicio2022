num = int(input('Digite um número n: '))
ultimo = 1
penultimo = 1

for i in range(2, num+1):
    numero = ultimo + penultimo
    penultimo = ultimo
    ultimo = numero
    print(numero, end = ' ')



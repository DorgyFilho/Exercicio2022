'''Faça um Programa que peça a temperatura em graus Celsius, 
transforme e mostre em graus Fahrenheit.'''

c = float(input('Temperatura em °C: '))
f = (c * 9/5) + 32
print(f'Celsius: {c:.1f}°C -> Fahreinheit: {f:.1f}°F')
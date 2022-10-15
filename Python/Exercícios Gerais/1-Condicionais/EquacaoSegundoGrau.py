
ax = int(input('Coeficiente a: '))
bx = int(input('Coeficiente b: '))
c = int(input('Coeficiente c: '))

if ax == 0:
    print('Não é equação do segundo grau.')
else:
    delta = (bx*bx) - (4*ax*c)
    if delta < 0:
        print('Não há raízes para esta equação')
    elif delta == 0:
        x = (-bx + 2*(delta**0.5))//(2*ax)
        print(f'A raíz da equação é {x}')
    else:
        x1 = (-bx + 2*(delta**0.5))//(2*ax)
        x2 = (-bx - 2*(delta**0.5))//(2*ax)
        print(f'As raízes da equação são {int(x1)} e {int(x2)}')
 
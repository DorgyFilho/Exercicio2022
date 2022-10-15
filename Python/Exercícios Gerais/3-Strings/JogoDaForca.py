'''Jogo Da Forca'''

erros = 0
PalavraCerta = 'CAMARAGIBE'
Resposta = ''

while erros < 6:
    letra = input('Digite uma letra: ').upper()
    if letra in PalavraCerta:
        Resposta += letra

        sublinhados = 0

        for i in PalavraCerta:
            if i in Resposta:
                print(i, end=' ')
            else:
                print('_', end=' ')
                sublinhados += 1
    
        if erros == 0 and sublinhados == 0:
            print(f'Vitória perfeita! Resposta certa é {PalavraCerta}')
            break
        elif (0 < erros < 6) and sublinhados == 0:
            print(f'Você venceu! Palavra certa é {PalavraCerta}')
            break
    else:
        erros += 1
        print(f'Você errou a {erros}° tentativa.')
else:
    print(f'Infelizmente você perdeu o jogo. A resposta certa é {PalavraCerta}')
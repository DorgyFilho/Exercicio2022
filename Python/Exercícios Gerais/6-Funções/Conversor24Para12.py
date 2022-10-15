'''Conversor 24 para 12 horas'''

def Conversor(hora):
    Contador = 0
    if hora > 12 and hora != 24:
        Contador = 0
        for i in range(hora):
            if i >= 12:
                Contador += 1
        return Contador
        
    elif hora == 24:
        return 0
    else:
        if 0 <= hora < 12:
            return hora
        elif 12 <= hora < 24:
            return hora-12
        else:
            return 'Hora inválida'

def Main():

    while True:
        hora = input('Digite a hora -> ').upper()
        minuto = input('Digite o minuto -> ').upper()
        
        if hora == 'N' or minuto == 'N':
            print('Programa encerrado')
            break
        else:
            horaInt = int(hora)
            minutoInt = int(minuto)
            HoraConvertida = Conversor(horaInt)
            print(f'{horaInt}:{minutoInt} -> {HoraConvertida}:{minutoInt}')
           

Main()
'''Calculadora IMC'''
from tkinter import *

'''Parte Operacional'''
App = Tk()
InserirPeso = IntVar(None)
InserirAltura = IntVar(None)
Resultado = IntVar(None)

def CalcularIMC():
    
    try:
        Result = float(Peso.get())/(float(Altura.get())*float(Altura.get()))

        if Result < 18.5:
            TextoResult.set('Abaixo do Peso Ideal')
        elif 18.5 <= Result < 25:
            TextoResult.set('Peso Normal')
        elif 25 <= Result < 30:
            TextoResult.set('Sobrepeso')
        elif 30 <= Result < 35:
            TextoResult.set('Obesidade')
        elif 35 <= Result < 40:
            TextoResult.set('Obesidade II')
        else:
            TextoResult.set('Obesidade Mórbida')
        Resultado.set(f'{Result:.1f}')
    
    except ZeroDivisionError:
        InserirPeso.set()
        InserirAltura.set()
        Resultado.set()

'''Parte Gráfica'''
App.title('Calculadora de IMC')

InfoTexto = StringVar()
InfoTexto.set('Informação\n< 18.5: Abaixo do Peso\n18.5 - 24.9: Peso Normal\n25 - 29.9: Acima do Peso\n30 - 34.9: Obesidade I\n35 - 39.9: Obesidade II\nAcima de 40: Obesidade Mórbida\n')
InfoLabel = Label(App, textvariable=InfoTexto)
InfoLabel.pack()

PesoTexto = StringVar()
PesoTexto.set('Digite seu peso')
PesoLabel = Label(App, textvariable=PesoTexto)
PesoLabel.pack()

Peso = Entry(App, textvariable=InserirPeso)
Peso.pack()

AlturaTexto = StringVar()
AlturaTexto.set('\nDigite sua altura em m.')
AlturaLabel = Label(App, textvariable=AlturaTexto)
AlturaLabel.pack()

Altura = Entry(App, textvariable=InserirAltura)
Altura.pack()

Button(App, text='Calcule seu IMC', font=('Kalimati', 12), command=CalcularIMC).pack(padx=10, pady=10)
Label(App, text='\nResultado').pack()

TextoLabel = Entry(App, textvariable=Resultado)
TextoLabel.pack()

TextoResult = StringVar()
TextoResult.set('Seu Resultado')
ResultTextoLabel = Label(App, textvariable=TextoResult)
ResultTextoLabel.pack()


#Executar o programa
App.mainloop()
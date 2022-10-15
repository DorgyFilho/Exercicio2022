from random import choice
import string as char
from tkinter import *

Janela = Tk()
Resultado = StringVar(None)

def GerarSenhaAutomatica():
    tamanho = 8
    valores = char.ascii_letters + char.digits + char.punctuation
    senha = ''
    for tam in range(tamanho):
        senha += choice(valores)
    Resultado.set(f'{senha}')

Janela.geometry('640x480')
Janela.title('Gerador de Senha Automática')

Button(Janela, text='Gerar Senha', font=('Kalimati', 10), command=GerarSenhaAutomatica).pack(padx=10, pady=10)
Label(Janela, text='A sua senha é')

TextoLabel = Label(Janela, textvariable=Resultado)
TextoLabel.pack()

Janela.mainloop()





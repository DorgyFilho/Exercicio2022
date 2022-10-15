from tkinter import *
from random import *

FaceDados = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
Total = 0

def RolarDados():

    #Declaração de variável global
    global Total
    
    #Rolar os dados
    dado = choice(FaceDados)

    #Obter o resultado
    ResultadoDado = Resultado(dado)

    #Exibir o Resultado
    DesenhoDados.config(text=dado)

    #Mostrar quantos pontos você conseguiu.
    UpdatePontos.config(text=f'Você conseguiu {ResultadoDado} pontos')
    
    #Calcular o total
    Total += ResultadoDado

    #Mostrar o total de pontos
    TotalPontos.config(text=f'O total de pontos é de {Total}')

def Resultado(num):
    if num == '\u2680':
        return(1)
    elif num == '\u2681':
        return(2)
    elif num == '\u2682':
        return(3)
    elif num == '\u2683':
        return(4)
    elif num == '\u2684':
        return(5)
    elif num == '\u2685':
        return(6)


#Criar Janela
Jogo = Tk()
Jogo.title('Jogo de Dados')
Jogo.geometry('500x500')

#Fazer o jogo funcionar
Jogar = Frame(Jogo)
Jogar.pack(pady=20)
    
#Desenhar as faces dos dados
DesenhoDados = Label(Jogar, text='', font=('Helvetica', 80), fg='white')
DesenhoDados.grid(padx=5, row = 0, column = 1)
SubDesenho = Label(Jogar, text='')
SubDesenho.grid(row=1, column=1)

#Botao Para Acionar o jogo
BotaoJogar = Button(Jogar, text='Role os Dados', font=('Helvetica', 12), command=RolarDados)
BotaoJogar.grid(row=3, column=1)

#Exibir Mensagem dos Pontos
UpdatePontos = Label(Jogar, text='', font=('Helvetica', 12))
UpdatePontos.grid(row=5, column=1)

#Exibir Total dos Pontos
TotalPontos = Label(Jogar, text='', font=('Helvetica', 12))
TotalPontos.grid(row=7, column=1)

Jogo.mainloop()
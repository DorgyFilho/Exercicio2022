import os as sistema

def Renomeador(nomeArq, caminho):

    contador = 0
    NomeArq = str(nomeArq)
    Caminho = str(caminho)
    for filename in sistema.listdir(Caminho):
        Origem = Caminho + '/' + filename
        Destino = Caminho + '/' + NomeArq + str(contador) + '.jpg'
        sistema.rename(Origem, Destino)
        contador += 1

def Main():

    Resposta = 'S'
    while Resposta == 'S':
        arquivo = input('Digite o nome-base do arquivo: ')
        caminho = input('Digite o caminho da pasta: ')

        Renomeador(arquivo, caminho)
    
        Resposta = input('Deseja repetir a operação (S ou N): ').upper()
        if Resposta == 'N':
            print('Programa Encerrado.')
            break
        elif Resposta == 'S':
            continue
        else:
            print('Resposta Inválida')
            break

Main()


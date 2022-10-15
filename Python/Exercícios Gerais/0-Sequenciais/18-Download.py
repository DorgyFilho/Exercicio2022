'''Faça um programa que peça o tamanho de um arquivo para download (em MB) 
e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo 
aproximado de download do arquivo usando este link (em minutos).'''

TamanhoArquivo = input('Digite o tamanho em MB do arquivo: ')

try:
    TamanhoArquivo = float(TamanhoArquivo)
    VelocidadeLink = input('Digite a velocidade da internet em Mbps: ')

    try:
        VelocidadeLink = float(VelocidadeLink)
        TempoDownload = (TamanhoArquivo / VelocidadeLink)
        TempoMinutos = TempoDownload%60
        print(f'O tempo de download é de {int(TempoMinutos)} minutos')
    except:
        print('Informação inválida.')

except:
    print('Informação inválida.')
        

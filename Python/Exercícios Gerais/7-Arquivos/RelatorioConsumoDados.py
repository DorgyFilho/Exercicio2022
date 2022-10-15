'''A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor 
de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado 
pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, 
ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125
Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que 
gere um relatório, chamado "relatório.txt", no seguinte formato:
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB
O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, 
de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes 
deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do 
percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.'''


def Bytes2MB(tamBytes):
    valorConvertido = float(tamBytes)
    resultado = float(valorConvertido/(1024**2))
    return resultado

def espacoOcupado(lista, total):
    media = 0
    tamLista = len(lista)
    media = total/(tamLista+1)
    return media

def PercentualUsuario(lista, total):
    perc = (lista[3]/total)*100
    lista.insert(len(usuarios), perc)


ListaUsuarios = []
total = 0
media = 0
UsuariosPosicao = 1
with open('arquivo.txt') as Arq:

    valor = 0

    for i in Arq:
        ListaUsuarios.append(i.split())
        
    for usuarios in ListaUsuarios:
        usuarios.insert(0, UsuariosPosicao)
        valor = Bytes2MB(float(usuarios[2]))
        total += valor
        usuarios.insert(len(usuarios),valor)
        UsuariosPosicao += 1
        
    for usuarios in ListaUsuarios:
        PercentualUsuario(usuarios, total)
    
    media = espacoOcupado(usuarios, total)

with open('relatorio.txt', 'w') as NovoArq:
    NovoArq.write('ACME Inc.               Uso do espaço em disco pelos usuários.\n')
    NovoArq.write('-'*80)
    NovoArq.write('\nNr\t\t\t\tUsuário\t\t\t\tEspaço Utilizado\t\t\t\t% De Uso\n')

    for usuarios in ListaUsuarios:
        Taxa = f'{usuarios[3]:.1f}'
        NovoArq.write(f"{str(usuarios[0])}\t\t\t\t{str(usuarios[1])}\t\t\t\t{str(Taxa)}\tMB\t\t\t\t{float(usuarios[4]):.2f}%\n")

    NovoArq.write(f'Espaço total ocupado: {total:.2f} MB\n')
    NovoArq.write(f'Espaço médio ocupado: {media:.2f} MB')

with open('arquivo.txt') as Arquivo:
    Arquivo.readlines()




            
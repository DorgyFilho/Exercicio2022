#Lista de Convidados

ListaConvidados = []

#1 - Adicionar Nome Via Digitação
def Adicionar_Nome_Input():
    
    global ListaConvidados
    
    NomeCompleto = input('Digite o nome a ser adicionado: ')
    
    if NomeCompleto not in ListaConvidados:
        ListaConvidados.append(NomeCompleto)
        print('Convidado adicionado')
    else:
        print(f'{NomeCompleto} encontra-se na lista')

#2 - Adicionar nomes via arquivo
def Adicionar_Nome_ListaArquivo(arquivo):

    global ListaConvidados

    Abrir = open(arquivo, 'r')
    ListaAux = Abrir.readlines()
    Abrir.close()

    Aux2 = [nome.rstrip('\n\r') for nome in ListaAux]
    
    for convidado in Aux2:
        if convidado not in ListaConvidados:
            ListaConvidados.append(convidado)
            print(f'{convidado} foi Adicionado(a)')
        else:
            print(f'{convidado} já encontra-se na lista de convidados')

#3 - Pesquisar Por Nome
def Pesquisa_Nome():
    
    global ListaConvidados

    nome = input('Digite a sua pesquisa: ')
    if nome not in ListaConvidados:
        print(f'{nome} não encontra-se na lista de convidados.')
    else:
        print(f'{nome} está na lista de convidados.')

#4 - Remover Pessoa da Lista
def Remover_Nome_Lista():

    global ListaConvidados

    nome = input('Digite o nome: ')
    if nome in ListaConvidados:
        ListaConvidados.remove(nome)
        print('Nome removido da lista')
    else:
        print(f'{nome} não encontra-se na lista.')

#5 - Editar Nome
def Editar_Nome():

    global ListaConvidados

    print('Lista de Convidados - Antes')
    for nomes in ListaConvidados:
        print(nomes)

    print()
    nome = input('Busque o nome a ser editado: ')
    if nome in ListaConvidados:
        IndiceNome = ListaConvidados.index(nome)
        NovoNome = input('Digite o nome modificado: ')
        ListaConvidados[IndiceNome] = NovoNome
        print('Nome Alterado')
    else:
        print(f'{nome} não encontra-se na lista')
    
    print()
    print('Convidados Presentes')
    print()
    for convidado in ListaConvidados:
        print(f'{convidado}')


#6 - Exibir Lista de forma ordenada
def Exibir_Lista():

    global ListaConvidados

    print('Lista de Convidados')
    print()
    ListaConvidados.sort()
    for nomes in ListaConvidados:
        print(nomes)

#7 - Apagar Lista
def Apagar_Lista():

    global ListaConvidados

    if len(ListaConvidados) > 0:
        ListaConvidados.clear()
        print('Lista apagada')
    else:
        print('A lista não contém nenhum nome')




from listaconvidados import *

def Menu():

    print("Lista de Convidados. O que você deseja fazer?")
    print()
    print("\t     1 - Adicionar Nome input\n \
            2 - Adicionar arquivo-texto com nomes\n \
            3 - Pesquisar por convidado\n \
            4 - Remover convidado da lista\n \
            5 - Editar Nome\n \
            6 - Exibir Lista\n \
            7 - Apagar Lista\n \
            0 - Sair")
    print()

    while True:

        opcao = input('Digite uma opção: ')
        try:
            opcao = int(opcao)
            if opcao == 0:
                print('Programa encerrado.')
                break
            if opcao == 1:
                Adicionar_Nome_Input()
            elif opcao == 2:
                Arquivo = input('Digite o endereço de origem do seu arquivo: ')
                Adicionar_Nome_ListaArquivo(Arquivo)
            elif opcao == 3:
                Pesquisa_Nome()
            elif opcao == 4:
                Remover_Nome_Lista()
            elif opcao == 5:
                Editar_Nome()
            elif opcao == 6:
                Exibir_Lista()
            elif opcao == 7:
                Apagar_Lista()
        
        except:
            print('Opção Inválida')
Menu() 

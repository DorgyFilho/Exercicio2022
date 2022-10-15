'''Inserir Informação no dicionário'''

Agenda = {}
while True:
    registro = input('Digite o seu registro: ').upper()
    try:
        if registro == 'N':
            print('Programa encerrado.')
            break
        else:
            registro = int(registro)
            if registro not in Agenda:
                Nome = input('Digite seu nome: ')
                Agenda['Nome'] = Nome
                Agenda['Registro'] = registro
                Agenda = {'Nome': Nome, 'Registro': registro}
            else:
                print('Registro cadastrado. Insira um registro diferente')     
        print(Agenda)
    except:
        if type(registro) is not int:
            print('Apenas números são aceitos.')

'''Cadastro de Pessoas'''

Cadastro = {}
cpf = ''
while cpf != '0':
    cpf = input('Digite seu cpf: ')
    if cpf == '0':
        print('Programa encerrado.')
        break
    else:
        nome = input('Digite seu nome: ')
        email = input('Digite seu email: ')
        Cadastro[cpf] = {'Nome': nome, 'E-mail': email}
    print(Cadastro)

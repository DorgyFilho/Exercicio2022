agenda = {}
cpf = ''
while cpf != 0:
    cpf = int(input('CPF: '))
    if cpf == 0:
        print('Cadastramento Encerrado.')
    else:
        nome = input('Nome: ').upper()
        idade = int(input('Idade: '))
        fone = input('Telefone: ')
        agenda[cpf] = {'Nome': nome, 'Idade': idade, 'Telefone': fone}
print(agenda)
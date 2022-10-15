'''Faça um programa que leia um nome de usuário e a sua senha e não aceite 
a senha igual ao nome do usuário, mostrando uma mensagem de 
erro e voltando a pedir as informações.'''

login = ''
senha = ''
LoginCadastrado = ''
SenhaCadastrada = ''
while login == senha:
    print('O login e a senha precisam ser diferentes.')
    login = input('Digite login: ')
    senha = input('Digite a senha: ')
    if login == senha:
        continue
    else:
        LoginCadastrado = login
        SenhaCadastrada = senha
        print(f'Login: {LoginCadastrado} / Senha: {SenhaCadastrada}')
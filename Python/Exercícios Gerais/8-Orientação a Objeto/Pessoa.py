'''Pessoa'''

class Pessoa:

    def __init__(self):
        self.nome = ''
        self.email = ''
        self.telefone = ''
        self.dicionario = {}
    
    def Cadastro(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.dicionario = {'Nome': self.nome, 'E-mail': self.email, 'Telefone': self.telefone}
    
    def MostraDados(self):
        print(self.dicionario)

def Main():

    resposta = 'S'
    while resposta == 'S':
        nome = input('Nome: ')
        email = input('E-mail: ')
        telefone = input('Telefone: ')
        Cadastrar = Pessoa()
        Cadastrar.Cadastro(nome, email, telefone)

        Cadastrar.MostraDados()

        resposta = input('Repetir?: ').upper()
        if resposta == 'N':
            print('Programa encerrado.')
            break
        elif resposta == 'S':
            continue
        else:
            print('Opção inválida.')
Main()
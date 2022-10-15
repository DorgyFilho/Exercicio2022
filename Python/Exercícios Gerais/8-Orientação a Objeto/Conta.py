'''Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 
A classe deve possuir os seguintes atributos: número da conta, nome do 
correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e 
saque; No construtor, saldo é opcional, com valor default zero e os demais 
atributos são obrigatórios.'''


class Conta:

    def __init__(self, conta = '', nome = '', saldo = 0):
        self.__conta = conta
        self.__nome = nome
        self.__saldo = saldo
    
    def Deposito(self, valor):
        try:
            valor = float(valor)
            if valor > 0:
                self.__saldo += valor
                return f'Nome: {self.__nome}\nConta: {self.__conta}\nSaldo: {self.__saldo}'
            else:
                return 'Apenas valores maiores que R$ 0 são permitidos.'
        except:
            return 'Informação inválida'

    
    def Saque(self, valor):
        try:
            valor = float(valor)
            if self.__saldo > valor:
                self.__saldo -= valor
                return f'Nome: {self.__nome}\nConta: {self.__conta}\nSaldo: {self.__saldo}'
            else:
                return 'O valor selecionado é superior ao valor do saldo.'
        except:
            return 'Informação inválida.'
    
    def AlterarNome(self, novoNome):
        self.__nome = novoNome
        return f'O nome agora é {self.__nome}'
    
    def MostrarStatus(self):
        return f'Nome: {self.__nome}\nConta: {self.__conta}\nSaldo: {self.__saldo}'

def Main():

    repetir = 'S'
    while repetir == 'S':
        nome = input('Nome: ')
        conta = input('Conta: ')
        saldo = input('Saldo: ')
        try:
            saldo = int(saldo)
            Cliente = Conta(nome, conta, saldo)
            print('Qual opção você deseja:\n1-Depósito\n2-Saque\n3-Alterar Nome\n4-Mostrar Saldo\n')
            opcao = input('Escolha a opção: ')
            try:
                opcao = int(opcao)
                if opcao == 1:
                    print(Cliente.Deposito(input('Valor a ser depositado: ')))
                elif opcao == 2:
                    print(Cliente.Saque(input('Valor a ser sacado: ')))
                elif opcao == 3:
                    print(Cliente.AlterarNome(input('Digite o novo nome: ')))
                elif opcao == 4:
                    print(Cliente.MostrarStatus())
                else:
                    print('Opção Inválida')
            except:
                print('Opção Inválida.')
        except:
            print('Informação inválida')
        

        print('Deseja realizar mais alguma operação? S-Sim ou N-Não\n')
        repetir = input('Resposta: ').upper()
        if repetir == 'N':
            print('Programa encerrado. Obrigado(a) e volte sempre.')
        elif repetir == 'S':
            continue
        else:
            print('Opção inválida.')
            break

Main()



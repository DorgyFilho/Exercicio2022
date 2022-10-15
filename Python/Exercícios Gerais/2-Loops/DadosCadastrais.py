'''Dados Cadastrais

Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';


'''

Recebe_Nome = ''
Recebe_Idade = 0
Recebe_Salario = 0
Recebe_Sexo = ''
Recebe_EstCivil = ''

def Nome(nome):
    global Recebe_Nome
    while len(nome) < 3:
        nome = input('Digite o nome: ')
        if len(nome) >= 3:
            Recebe_Nome = nome
        else:
            print('Inválido')

def Idade(idade):
    global Recebe_Idade
    try:
        idade = int(idade)
        while not (0 < idade < 150):
            idade = input('Digite a idade: ')
            try:
                idade = int(idade)
                if 0 < idade < 150:
                    Recebe_Idade = idade
                    Recebe_Idade = str(Recebe_Idade)
                else:
                    print('Idade fora do intervalo entre 0 e 150.')
            except:
                print('Informação inválida')
    except:
        return 'Informação inválida.'
    
def Salario(salario):
    global Recebe_Salario
    try:
        salario = float(salario)
        while salario < 0:
            salario = input('Digite o salário: ')
            try:
                salario = float(salario)
                if salario >= 0:
                    Recebe_Salario = salario
                    Recebe_Salario = str(Recebe_Salario)
                else:
                    print('Salário não pode ser menor que 0.')
            except:
                print('Informação inválida')
    except:
        return 'Informação inválida.'

def Sexo(sexo):
    global Recebe_Sexo
    while sexo not in ('M', 'F'):
        sexo = input('Digite o sexo: ').upper()
        if sexo in ('M', 'F'):
            Recebe_Sexo = sexo
        else:
            print('Informação inválida')

def Estado_Civil(estcivil):
    global Recebe_EstCivil
    while estcivil not in ('S', 'C', 'D', 'V'):
        estcivil = input('Estado civil (S, C, D, V): ').upper()
        if estcivil in ('S', 'C', 'D', 'V'):
            Recebe_EstCivil = estcivil
        else:
            print('Digite a opção válida')

def GuardaDados():
    Arq = open('Cadastro.txt', 'a')
    Arq.write(f'Nome: {Recebe_Nome}, Idade: {Recebe_Idade}, Salario: R${Recebe_Salario}, Sexo: {Recebe_Sexo}, Estado Civil: {Recebe_EstCivil}\n')
    Arq.close()

def Main():

    repetir = 'S'
    while repetir == 'S':
        Nome(input('Digite o nome: '))
        Idade(input('Digite a sua idade: '))
        Salario(input('Digite o salário: '))
        Sexo(input('Digite o sexo (M ou F): ').upper())
        Estado_Civil(input('Seu estado civil (S, C, D, V): ').upper())
        GuardaDados()

        print('Deseja repetir a operação (S/N)?')
        repetir = input('Resposta: ').upper()
        if repetir == "N":
            print('Programa encerrado')
            break
        elif repetir == "S":
            continue
        else:
            print('Informação inválida')
            break

Main()




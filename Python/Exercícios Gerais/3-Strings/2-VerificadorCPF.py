'''Verificação de CPF. Desenvolva um programa que solicite a digitação de 
um número de CPF no formato xxx.xxx.xxx-xx.'''

def ValidadorCPF(cpf):

    AuxCpf = cpf
    try:
        if AuxCpf[3] == '.' and AuxCpf[7] == '.' and AuxCpf[11] == '-':
            print(f'O cpf {AuxCpf} é válido')
        else:
            print('Formato do CPF inválido.')
    except:
        print('Informação inválida.')

def main():

    while True:
        cpf = input('Digite o cpf no formato xxx.xxx.xxx-xx: ')
        if cpf == '':
            print('Programa encerrado.')
            break
        else:
            ValidadorCPF(cpf)

main()
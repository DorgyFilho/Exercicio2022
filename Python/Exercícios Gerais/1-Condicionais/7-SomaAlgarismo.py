# '''Escreva um programa que leia um numero inteiro maior do que zero e devolva, 
# na tela, a soma de todos os seus algarismos. Por exemplo, ao numero 251 
# corresponder ao valor 8 (2 + 5 + 1). Se o numero lido nao for maior do que zero, o programa terminar ˜ a com a ´
# mensagem “Numero invalido”.'''

num = input('Digite um número: ')
try:
    Soma = 0
    num = int(num)
    ListaNum = []
    if num >= 0:
        StrNum = str(num)
        RepStrNum = StrNum.replace("",",")[1:-1]
        SplitNum = RepStrNum.split(",")
        for i in SplitNum:
            Soma += int(i)

    StrAdd = ""
    for k in range(len(SplitNum)):
        StrAdd += SplitNum[k]
    StrAdd = StrAdd.replace('','+')[1:-1] 
    print(f'{Soma}({StrAdd})', end='')
except:
    print('Apenas valores numéricos positivos são permitidos')



# StrNum = '321'
# RepStrNum = StrNum.replace('', ',')[1:-1]
# Lista = RepStrNum.split(",")
# print(Lista)
# Soma = 0
# for i in Lista:
#     Soma += int(i)
# print(Soma)



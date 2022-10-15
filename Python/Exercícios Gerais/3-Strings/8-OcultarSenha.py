'''. Crie uma rotina que recebe como argumento duas Strings, sendo que uma
contém uma frase e outra contém uma expressão. O objetivo da rotina é
criar uma nova frase em que qualquer ocorrência da expressão dada como
segundo argumento é substituída por asteriscos ('*'). Por exemplo, se os
argumentos recebidos forem "A minha senha é " e "12345", a rotina
deverá devolver "A minha senha é *****"'''

Frase = input('Digite a frase: ')
Senha = input('Digite a senha: ')
TamSenha = len(Senha)
SenhaOculta = Senha.replace(Senha,"*"*TamSenha)

FraseCompleta = Frase + " " + SenhaOculta
print(f'{FraseCompleta}')
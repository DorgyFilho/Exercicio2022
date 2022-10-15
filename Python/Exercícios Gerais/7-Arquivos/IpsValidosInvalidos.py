'''Ips Validos e Inválidos'''

validos = ''
invalidos = ''
with open('ip.txt', 'r') as Arq:
    ListaIps = Arq.readlines()
    validos = ''
    invalidos = ''
    for i in range(len(ListaIps)):
        ip = ListaIps[i].split('.')
        if int(ip[0]) < 255 and int(ip[1]) < 255 and int(ip[2]) < 255 and int(ip[3]) < 255:
            validos += ListaIps[i] + "\n"
        else:
            invalidos += ListaIps[i] + "\n"

with open('IpTratado.txt', "a") as Arc:
    Arc.write("Ip's válidos\n"+"\n"+validos+"\n")
    Arc.write("Ip's inválidos\n"+"\n"+invalidos+"\n")

print('Operação realizada')
    



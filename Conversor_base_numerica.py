#NUMERIC BASE CONVERTER
#DATA: 09/05/22
#PROGRAMADOR: YANGZ

#BIBLIOTECA DE CONTROLE DE TEMPO
from time import sleep

#TERMINAL COLOR
reset = '\033[37m'
red = '\033[91m'
green = '\033[92m'
yellow = '\033[93m'
blue = '\033[94m'

#CABEÇALHO
def cabecalho():
    print(red,"-=" *20)
    print(reset,"{:^40}".format("CONVERSOR"))
    print(red,'-=' *20,reset)

#MENU
def menu():
    global usuario
    #ENTRADA DE DADOS
    num = int(input(" Digite um número inteiro: "))
    print(red,"-=" *20)
    sleep(1)
    print (reset,"{:^40}".format("||   MENU   ||"))
    print (red,"--" * 20,reset)
    print(green,"[ 1 ]",reset,"Converter para",green,"BINÁRIO")
    print(yellow,"[ 2 ]",reset,"Converter para",yellow,"OCTAL")
    print(blue,"[ 3 ]",reset,"Converter para",blue,"HEXADECIMAL")
    print(red,"[ 4 ]",reset,"Sair")
    print(" ")
    usuario = int(input("Digite uma opção: "))
    print(red,"-=" *20)

    binario = bin(num)[2:]
    octal = oct(num)[2:]
    hexadecimal = hex(num)[2:]
    #ESTRUTURA CONDICIONAL
    if usuario == 1:
        print(green,f'{num}',reset,'Convertido para',green,'BINÁRIO',reset,'é',green,f'{binario}')
        print(red,"-=" *20,reset)

    elif usuario == 2:
        print(yellow,f'{num}',reset,'Convertido para',yellow,'OCTAL',reset,'é',yellow,f'{octal}')
        print(red,"-=" *20,reset)

    elif usuario == 3:
        print(blue,f'{num}',reset,'Convertido para',blue,'HEXADECIMAL',reset,'é',blue,f'{hexadecimal}')
        print(red,"-=" *20,reset)

    elif usuario == 4:
        sair = True
    else:
        print(red,"{:^40}".format("-- ERRO!!! Opção Inválida  --"))
        print(red,"-=" * 20,reset)

cabecalho()
sair = False
while not sair:
    menu()
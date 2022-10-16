#IMC
#PROGRAMADOR: YANGZ
#DATA: 09/05/22

#V1 - Programa que calcula o IMC de uma pessoa
#++ loop
#++ menu de 4 opções e se não forem escolhidas dará erro

#BIBLIOTECA DE CONTROLE DE TEMPO
from time import sleep

#TERMINAL COLOR
reset = '\033[37m'
red = '\033[91m'
green = '\033[92m'
yellow = '\033[93m'
blue = '\033[94m'

#LIMPAR
def limpar():
    print("\n" * 100)
#CABEÇALHO
def cabecalho():
    print(red,"-=" *20)
    print(yellow,"{:^40}".format("CALCULADORA IMC"))
    print(red,'-=' *20)
#MENU
def menu():
    global usuario
    print (yellow,"{:^40}".format("||   MENU   ||"))
    print (red,"--" * 20)
    print(green," [1]", reset,"Calcular IMC \n",green,"[2]",reset,"Mostrar tabela de referencia \n",yellow,"[3]",reset,"Limpar terminal \n",red,"[4]",reset,"Sair",yellow)
    print(" ")
    usuario = int(input("Digite uma opção: "))
#FORMULÁRIO
def formularioEntrada():
    #DISPLAY
    print(red,'-=' *20)
    print(yellow,"{:^40}".format("||   INFORME   ||"))
    print(red,'-=' *20,reset)

    #ENTRADA DE DADOS
    global nome, sexo, idade, peso, altura, imc

    nome = str(input("--> Nome: "))
   
    #ESTRUTURA CONDICIONAL - SEXO
    sexo = str(input("--> Sexo (M/F): "))
    if sexo == "M" or "m":
        sexo = "Masculino"
    elif sexo == "F" or "f":
        sexo = "Feminino"
    
    idade = (input("--> Idade: ")) 

    #DADOS PRINCIPAIS      
    peso =  float(input('--> Qual é seu peso (Kg): '))
    altura = float(input('--> Qual é sua altura (m): '))
    print(red,'-=' *20)
#IMC
def estruturaIMC():
    print(yellow,"--> O IMC desta pessoa é de",green,"{:.1f}".format(imc))
    if imc < 18.5:
        print(yellow,'--> Voce está',red,'ABAIXO DO PESO',yellow,'normal')
    elif 18.6 <= imc < 25:
        print(yellow,'--> Voce está no',green,'PESO IDEAL')
    elif 25 <= imc < 30:
        print(yellow,'--> Voce está com SOBREPESO')
    elif 30 <= imc < 35:
        print(yellow,'--> Voce está com',red,'OBESIDADE GRAU I')
    elif 35 <= imc < 40:
        print(yellow,'--> Voce está com',red,'OBESIDADE GRAU II (severa)')
    else:
        print(yellow,'--> Voce está com',red,'OBESIDADE GRAU III (mórbida)')
#RELATORIO
def relatorio():
    sleep(1)
    print(green,"{:^40}".format("---> RELATÓRIO <---"))
    print(red,"--" * 20)
    estruturaIMC()
    print(red,"-=" * 20)
    sleep(1)
#TABELA INFORMATIVA
def tabelaInfo():
        print(red,"-=" * 20)
        print("{:^40}".format("--> TABELA INFORMATIVA IMC <--"))
        print(red,"--" * 20)
        print(yellow,"IMC < 18.5:",red,"ABAIXO DO PESO")
        print(yellow,"IMC < 25:",green,"PESO IDEAL")
        print(yellow,"IMC < 30:",yellow,"SOBREPESO")
        print(yellow,"IMC < 35:",red,"OBESIDADE GRAU I")
        print(yellow,"IMC < 40:",red,"OBESIDADE GRAU II (severa)")
        print(yellow,"IMC > 40:",red,"OBESIDADE GRAU III (mórbida)")
        print(red,"-=" * 20)

#EXECUÇÃO
cabecalho()
sair = False
while not sair:
    menu()
    sleep(1)
    #ESTRUTURA CONDICIONAL - MENU
    #CALCULA IMC
    if usuario == 1:
        formularioEntrada()

        #PREOCESSAMENTO DE DADOS
        imc = peso / (altura ** 2)

        #RELATORIO
        relatorio()
        sleep(1)
    #MOSTRA TABELA INFORMATIVA
    elif usuario == 2:
        tabelaInfo()
        sleep(1)
   #LIMPA TELA
    elif usuario == 3:
        limpar()
        cabecalho()
    #ENCERRA O PROGRAMA PROGRAMA
    elif usuario == 4:
        sair = True
    #ERRO   
    else:
        print(red,"-=" * 20)
        print(red,"{:^40}".format("-- ERRO!!! Opção Inválida  --"))
        print(red,"-=" * 20)

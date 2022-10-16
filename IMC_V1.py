#IMC
#PROGRAMADOR: YANGZ
#DATA: 09/05/22

#V1 - Programa que calcula o IMC de uma pessoa
#++ loop
#++ menu de 4 opções e se não forem escolhidas dará erro

#BIBLIOTECA DE CONTROLE DE TEMPO
from time import sleep

#LIMPAR
def limpar():
    print("\n" * 100)
#CABEÇALHO
def cabecalho():
    print("-=" *20)
    print("{:^40}".format("CALCULADORA IMC"))
    print('-=' *20)
#MENU
def menu():
    global usuario
    print ("{:^40}".format("||   MENU   ||"))
    print ("--" * 20)
    print("[1] Calcular IMC \n[2] Mostrar tabela de referencia \n[3] Limpar terminal \n[4] Sair")
    print(" ")
    usuario = int(input("Digite uma opção: "))
#FORMULÁRIO
def formularioEntrada():
    #DISPLAY
    print('-=' *20)
    print("{:^40}".format("||   INFORME   ||"))
    print('-=' *20)

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
    print('-=' *20)
#IMC
def estruturaIMC():
    print('--> O IMC desta pessoa é de {:.1f}'.format(imc))
    if imc < 18.5:
        print('--> Voce está ABAIXO DO PESO normal')
    elif 18.6 <= imc < 25:
        print('--> Voce está no PESO IDEAL')
    elif 25 <= imc < 30:
        print('--> Voce está com SOBREPESO')
    elif 30 <= imc < 35:
        print('--> Voce está com OBESIDADE GRAU I')
    elif 35 <= imc < 40:
        print('--> Voce está com OBESIDADE GRAU II (severa)')
    else:
        print('--> Voce está com OBESIDADE GRAU III (mórbida)')
#RELATORIA
def relatorio():
    sleep(1)
    print("{:^40}".format("---> RELATÓRIO <---"))
    print("--" * 20)
    estruturaIMC()
    print("-=" * 20)
    sleep(1)
#TABELA INFORMATIVA
def tabelaInfo():
        print("-=" * 20)
        print("{:^40}".format("--> TABELA INFORMATIVA IMC <--"))
        print("--" * 20)
        print("""IMC < 18.5: ABAIXO DO PESO\n
IMC < 25: PESO IDEAL\n
IMC < 30: SOBREPESO\n
IMC < 35: OBESIDADE GRAU I\n
IMC < 40: OBESIDADE GRAU II (severa)\n
IMC > 40: OBESIDADE GRAU III (mórbida)""")
        print("-=" * 20)

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
        print("-=" * 20)
        print("{:^40}".format("-- ERRO!!! Opção Inválida  --"))
        print("-=" * 20)

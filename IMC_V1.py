#IMC
#PROGRAMADOR: YANGZ
#DATA: 09/05/22

#V1 - Programa que calcula o IMC de uma pessoa

#BIBLIOTECA DE CONTROLE DE TEMPO
from re import M
import string
from time import sleep

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
    print("[1] Calcular IMC \n[2] Mostrar tabela de referencia \n[3] Sair")
    print(" ")
    usuario = int(input("Digite uma opção: "))

#FORMULÁRIO
def formularioEntrada():
    #DISPLAY
    print('-=' *20)
    print("{:^40}".format("||   INFORME   ||"))
    print('--' *20)

    #ENTRADA DE DADOS
    global nome, sexo, idade, peso, altura
    nome = (input("--> Nome: "))
    if nome != string:
        print("!!ERRO!! Entrada inválida")
        nome = (input("--> Nome: "))




    #ESTRUTURA CONDICIONAL - SEXO
    sexo = string(input("--> Sexo (M/F): "))
    if sexo == "M" or "m":
        print("Masculino")
    elif sexo == "F" or "f":
        print("Feminino")
    else:
        print("!!ERRO!! Entrada inválida")

    idade = int(input("--> Idade: "))       
    peso =  float, int(input('--> Qual é seu peso (Kg): '))
    altura = float(input('--> Qual é sua altura (m): '))
    print('--' *20)

def estruturaIMC():
    print('-- > O IMC desta pessoa é de {:.1f}'.format(imc))
    print("--" * 20)
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
#EXECUÇÃO
cabecalho()
#LAÇO
sair = False
while not sair:
    menu()
    #ESTRUTURA CONDICIONAL - MENU
    if usuario == 1:
        formularioEntrada()

        #PROCESSAMENTO DE DADOS
        imc = peso / (altura ** 2)

        #ESTRUTURA CONDICIONAL
        estruturaIMC()

    elif usuario == 2:
        print("2")
    
    elif usuario == 3:
        sair = True

    else:
        print("erro")

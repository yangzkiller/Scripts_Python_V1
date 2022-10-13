#IMC
#PROGRAMADOR: YANGZ
#DATA: 09/05/22

#V1 - Programa que calcula o IMC de uma pessoa

#CABEÇALHO
def cabecalho():
    print("-=" *20)
    print("{:^40}".format("CALCULADORA IMC"))
    print('-=' *20)

#MENU
def menu():
    print ("{:^40}".format("||   MENU   ||"))
    print ("--" * 20)
    print("[1] Calcular IMC \n[2] Mostrar tabela de referencia \n[3] Sair")
    print(" ")

#FORMULÁRIO
def formularioEntrada(peso,altura ):
    #DISPLAY
    print('-=' *20)
    print("{:^40}".format("||   INFORME   ||"))
    print('--' *20)
    #ENTRADA DE DADOS
    nome = (input("--> Nome: "))
    sexo = (input("--> Sexo: "))
    idade = (input("--> Idade: "))       
    peso =  float(input('Qual é seu peso (Kg): '))
    altura = float(input('Qual é sua altura (m): '))
    dados = nome, sexo, idade
    calc = peso / (altura ** 2)
    return calc

'''#ESTRUTURA CONDICIONAL
print('O IMC desta pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce está ABAIXO DO PESO normal')
elif 18.6 <= imc < 25:
    print('Voce está no PESO IDEAL')
elif 25 <= imc < 30:
    print('Voce está com SOBREPESO')
elif 30 <= imc < 35:
    print('Voce está com OBESIDADE GRAU I')
elif 35 <= imc < 40:
    print('Voce está com OBESIDADE GRAU II (severa)')
else:
    print('Voce está com OBESIDADE GRAU III (mórbida)')
'''
#EXECUÇÃO
cabecalho()

#LAÇO
sair = False
while not sair:
    menu()
    #ENTRADA DE DADOS
    usuario = int(input("Digite uma opção: "))

    #ESTRUTURA CONDICIONAL - MENU
    if usuario == 1:
        
       #formulario
        imc = (formularioEntrada(peso,altura))
        print (imc)

    elif usuario == 2:
        print("2")
    
    elif usuario == 3:
        sair = True

    else:
        print("erro")

#CALCULO ÁREA
#PROGRAMADOR: YANGZ
#DATA: 21/11/2022

def linha01():
    print("=-" *20)

def linha02():
    print("--" *20)

def cabecalho(title):
    linha01()
    print(title)
    linha01()

def menu(opcoes):
    global usuario
    linha01()
    print ("{:^40}".format("||   MENU   ||"))
    linha02()
    print(opcoes)
    print(" ")
    usuario = int(input(" Digite uma opção: "))
    linha01()
    

def area(larg, comp):
    a = larg * comp
    print(f"A área do terreno é: {larg} x {comp} = {a}m²")


#EXECUÇÃO
cabecalho("  --> CALCULO ÁREA TERRENO <--")
#LAÇO
sair = False
while not sair:
    menu("[1] Calcular área do terreno\n[2] Sair")
     #ESTRUTURAIS CONDICIONAIS - MENU

    #OPCAO - 1
    if usuario == 1:
        #ENTRADA DE DADOS
        l = float(input("Digite a largura (m): "))
        c = float(input("Digite o comprimento (m): "))
        linha02()
        area(l, c)

    #OPCAO - 2
    elif usuario == 2:
        print("{:^40}".format("-- Programa Encerrado --"))
        sair = True
    
    #ERRO
    else:
        print("{:^40}".format("-- ERRO!!! Opção Inválida  --"))
    

        
    
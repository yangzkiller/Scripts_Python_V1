#Conversor_temperatura
#DATA: 19/11/22
#PROGRAMADOR: YANGZ

#Programa que peça a temperatura em graus Fahrenheit,
#Transforme e mostre a temperatura em graus Celsius e vice-versa

#CORES TERMINAL
reset = '\033[1;37m'
red = '\033[1;31m'
green = '\033[1;32m'
blue = '\033[1;34m'
purple = '\033[1;35m'
yellow = '\033[1;33m'

#DISPLAY
print(red,"=-" *20)
print(reset,"    --> CONVERSOR TEMPERATURA <--")
print(red,"=-" *20)

#LAÇO
sair = True
while (sair == True): 
    #MENU
    print(reset,"             ||   MENU   ||")
    print(red,"--" *20);
    print(yellow," [1] Converter CELSIUS para FAHRENHEIT\n  [2] Converter FAHRENHEIT para CELSIUS\n",red,"[3] Sair",reset)
    print(" ")
    #ENTRADA DE DADOS
    opcao = int(input("Digite uma opção: "))
    print(red,"=-" *20,reset)

    #ESTRUTURA CONDICIONAL - MENU
    #OPÇÃO - 1
    if (opcao == 1):
        #COMANDO DE SAIDA/ENTRADA DE DADOS
        graus_C = float(input("Digite a temperatura: "))
           
        #VARIAVEL GRAUS_F RECEBE O VALOR DE 1.8 QUE É MULTIPLICADO
        #PELO VALOR DE GRAUS_C QUE É SOMADO COM 32
        graus_F = 1.8 * graus_C + 32
        
        #COMANDO DE SAIDA DE DADOS
        print(red,"--" *20)
        print(yellow,"A temperatura é: %.2f°F" % (graus_F))
        print(red,"=-" *20,reset)
                   
    #OPÇÃO - 2
    elif (opcao == 2):
        #COMANDO DE SAIDA/ENTRADA DE DADOS
        graus_F = float(input("Digite a temperatura: "))

        #A VARIAVEL GRAUS_C RECEBE O VALOR DE GRAUS_F 
        #MENOS 32 MULTIPLICADO POR 5 DIVIDIDO POR 9
        graus_C = (graus_F -32.0) * ( 5.0 /9.0 )

        #COMANDO DE SAIDA DE DADOS
        print(red,"--" *20)
        print(yellow,"A temperatura é: %.2f°C" % (graus_C))
        print(red,"=-" *20,reset)
    
    #OPÇÃO - 3
    elif (opcao == 3):
        print(red,"      --> PROGRAMA ENCERRADO <--");
        print("=-" *20,reset)
        sair = False
        
    #ERRO
    else: 
        print(red,"        !ERRO! Entrada Inválida")
        print("=-" *20,reset)

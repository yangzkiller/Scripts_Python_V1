#ANO BISSEXTO
#PROGRAMADOR: YANGZ
#DATA: 20/11/22

#CORES TERMINAL
reset = '\033[1;37m'
red = '\033[1;31m'
green = '\033[1;32m'
blue = '\033[1;34m'
purple = '\033[1;35m'
yellow = '\033[1;33m'

def cabecalho(title):
    print(red,"=-" *20,reset)
    print(title)
    print(red,"=-" *20,reset)


cabecalho("  --> CALCULADORA DE ANO BISSEXTO <--")

#LAÇO
sair = True
while (sair == True):

    #MENU
    print("             ||   MENU   ||")
    print(red,"--" *20,yellow)
    print("  [1] Calculo Bissexto\n",red,"[2] Sair",reset)
    print(" ")
    #ENTRADA DE DADOS
    opcao = int(input("Digite uma opção: "))
    print(red,"=-" *20,reset)
                        
    #ESTRUTURA CONDICIONAL - MENU
    #OPÇÃO - 1
    if (opcao == 1):
    #ENTRADA DE DADOS
        ano = int(input("Digite o Ano: "))
        print(red,"--" *20)

        #PROCESSAMENTO DE DADOS
        if(ano % 4 == 0):
            print(green,"--> Bissexto <--",reset)
            print(red,"=-" *20,reset)     
        else:
            print(red,"--> Não é Bissexto <--")
            print("=-" *20,reset)
                
    #OPÇÃO - 2
    elif (opcao == 2):
        print(red,"      --> PROGRAMA ENCERRADO <--")
        print("=-" *20,reset)
        sair = False
            
    #ERRO
    else:
        print(red,"        !ERRO! Entrada Inválida")
        print("=-" *20,reset)


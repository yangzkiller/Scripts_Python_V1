#ANO BISSEXTO
#PROGRAMADOR: YANGZ
#DATA: 20/11/22

#DISPLAY
print("=-" *20)
print("  --> CALCULADORA DE ANO BISSEXTO <--")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

#LAÇO
sair = True
while (sair == True):

    #MENU
    print("             ||   MENU   ||")
    print("--" *20)
    print("[1] Calculo Bissexto\n[2] Sair")
    print(" ")
    #ENTRADA DE DADOS
    opcao = int(input("Digite uma opção: "))
    print("=-" *20)
                        
    #ESTRUTURA CONDICIONAL - MENU
    #OPÇÃO - 1
    if (opcao == 1):
    #ENTRADA DE DADOS
        ano = int(input("Digite o Ano: "))
        print("--" *20)

        #PROCESSAMENTO DE DADOS
        if(ano % 4 == 0):
            print("--> Bissexto <--")
            print("=-" *20)     
        else:
            print("--> Não é Bissexto <--")
            print("=-" *20)
                
    #OPÇÃO - 2
    elif (opcao == 2):
        print("      --> PROGRAMA ENCERRADO <--")
        print("=-" *20)
        sair = False
            
    #ERRO
    else:
        print("        !ERRO! Entrada Inválida")
        print("=-" *20)

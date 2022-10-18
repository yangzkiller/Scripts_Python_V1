#MÉDIA DE NOTAS 
#PROGRAMADOR: YANGZ
#DATA: 18/10/22

#V1 - Boletim escolar que recebe quantas notas o usuario quer

#BIBLIOTECA DE CONTROLE DE TEMPO
from time import sleep

#TERMINAL COLOR
reset = '\033[37m'
red = '\033[91m'
green = '\033[92m'
yellow = '\033[93m'
blue = '\033[94m'

#CABECALHO
print(red,"-=" * 20)
print (yellow,"{:^40}".format("Boletim Escolar"))
print(red,"-=" * 20)
sleep(1)

#LAÇO
sair = False
while not sair:
    #MENU
    print (yellow,"{:^40}".format("||   MENU   ||"))
    print (red,"--" * 20)
    print(green," [1]",reset,"Calcular média de 2 notas\n",green,"[2]",reset,"Calcular média de 4 notas\n",red,"[3]",reset,"Sair",yellow)
    print(" ")
    usuario = int(input(" Digite uma opção: "))
    print(red,"==" *20,reset)

    #ESTRUTURAIS CONDICIONAIS - MENU
    #OPCAO - 1
    if usuario == 1:
        #ENTRADA DE DADOS
        nota_1 = float(input("Digite a nota da  1° Prova: "))
        nota_2 = float(input("Digite a nota do  2° Prova: "))
        print(red,"--" * 20)

        #PROCESSAMENTO
        s = nota_1 + nota_2 
        media = s / 2
    
        #ESTRUTURA CONDICIONAL - APROVAÇÃO

        #APROVADO
        if media >= 6 :
            print(yellow,"Aluno",green,"(APROVADO)",yellow,"com média:",green,f"{media:.2f}")
            print(red,"==" * 20)
            sleep(1)
        #REPROVADO
        else:
            print(yellow,"Aluno",red,"(REPROVADO)",yellow,"com média:",red,f"{media:.2f}")   
            print(red,"--" * 20,reset)
            sleep(1)
        
    #OPCAO - 2
    elif usuario == 2:
        #ENTRADA DE DADOS
        nota_1 = float(input("Digite a nota da  1° Prova: "))
        nota_2 = float(input("Digite a nota do  2° Prova: "))
        nota_3 = float(input("Digite a nota da  3° Prova: "))
        nota_4 = float(input("Digite a nota do  4° Prova: "))
        print(red,"--" * 20)

        #PROCESSAMENTO
        s = nota_1 + nota_2 + nota_3 + nota_4
        media = s / 4
    
        #ESTRUTURA CONDICIONAL - APROVAÇÃO

        #APROVADO
        if media >= 6 :
            print(yellow,"Aluno",green,"(APROVADO)",yellow,"com média:",green,f"{media:.2f}")
            print(red,"==" * 20)
            sleep(1)
        #REPROVADO
        else:
            print(yellow,"Aluno",red,"(REPROVADO)",yellow,"com média:",red,f"{media:.2f}")   
            print(red,"--" * 20)
            sleep(1)
        
    #OPCAO - 3
    elif usuario == 3:
        sleep(1)
        print(yellow,"{:^40}".format("-- Programa Encerrado --"))
        print(red,"==" * 20,reset)
        sleep(1)
        sair = True

    #ERRO
    else:
        sleep(1)
        print(red,"{:^40}".format("-- ERRO!!! Opção Inválida  --"))
        print(red,"==" * 20)


#MÉDIA DE NOTAS 
#PROGRAMADOR: YANGZ
#DATA: 18/10/22

#V1 - Boletim escolar que recebe quantas notas o usuario quer

#BIBLIOTECA DE CONTROLE DE TEMPO
from time import sleep

#CABECALHO
print("-=" * 20)
print ("{:^40}".format("Boletim Escolar"))
print("-=" * 20)
sleep(1)

#LAÇO
sair = False
while not sair:
    #MENU
    print ("{:^40}".format("||   MENU   ||"))
    print ("--" * 20)
    print("[1] Calcular média de 2 notas\n[2] Calcular média de 4 notas\n[3]Sair")
    print(" ")
    usuario = int(input("Digite uma opção: "))
    print("==" *20)

    #ESTRUTURAIS CONDICIONAIS - MENU
    #OPCAO - 1
    if usuario == 1:
        #ENTRADA DE DADOS
        nota_1 = float(input("Digite a nota da  1° Prova: "))
        nota_2 = float(input("Digite a nota do  2° Prova: "))
        print("--" * 20)

        #PROCESSAMENTO
        s = nota_1 + nota_2 
        media = s / 2
    
        #ESTRUTURA CONDICIONAL - APROVAÇÃO

        #APROVADO
        if media >= 6 :
            print(f"Aluno (APROVADO) com média: {media:.2f}")
            print("==" * 20)
            sleep(1)
        #REPROVADO
        else:
            print(f"Aluno (REPROVADO) com média: {media:.2f}")   
            print("--" * 20)
            sleep(1)
        
    #OPCAO - 2
    elif usuario == 2:
        #ENTRADA DE DADOS
        nota_1 = float(input("Digite a nota da  1° Prova: "))
        nota_2 = float(input("Digite a nota do  2° Prova: "))
        nota_3 = float(input("Digite a nota da  3° Prova: "))
        nota_4 = float(input("Digite a nota do  4° Prova: "))
        print("--" * 20)

        #PROCESSAMENTO
        s = nota_1 + nota_2 + nota_3 + nota_4
        media = s / 4
    
        #ESTRUTURA CONDICIONAL - APROVAÇÃO

        #APROVADO
        if media >= 6 :
            print(f"Aluno (APROVADO) com média: {media:.2f}")
            print("==" * 20)
            sleep(1)
        #REPROVADO
        else:
            print(f"Aluno (REPROVADO) com média: {media:.2f}")   
            print("--" * 20)
            sleep(1)
        

    #OPCAO - 3
    elif usuario == 3:
        sleep(1)
        print("{:^40}".format("-- Programa Encerrado --"))
        print("==" * 20)
        sleep(1)
        sair = True

    #ERRO
    else:
        sleep(1)
        print("{:^40}".format("-- ERRO!!! Opção Inválida  --"))
        print("==" * 20)

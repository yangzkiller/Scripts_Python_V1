#BOLETIM UNISAN 
#PROGRAMADOR: YANGZ

#VERSÃO - V1 - Boletim escolar com nota de 2 bimestres, sendo a segunda nota tendo peso dois.
#DATA: 12/05/22

#BIBLIOTECA DE CONTROLE DE TEMPO
from time import sleep

#DISPLAY
print("-=" * 20)
print ("{:^40}".format("Boletim Escolar"))
print("-=" * 20)
sleep(1)

#LAÇO
sair = False
while not sair:
    #MENU
    sleep(1)
    print ("{:^40}".format("||   MENU   ||"))
    print ("--" * 20)
    print("[1] Calcular média das notas \n[2] Sair")
    print(" ")
    usuario = int(input("Digite uma opção: "))
    print("==" *20)

    #ESTRUTURAIS CONDICIONAIS MENU
    #OPCAO - 1
    if usuario == 1:
        #ENTRADA DE DADOS
        P1 = float(input("Digite a nota da  1° Prova: "))
        P2 = float(input("Digite a nota do  2° Prova: "))

        #PROCESSAMENTO
        s = P1 * 1 + P2 * 2
        media = s / 3
    
        #ESTRUTURA CONDICIONAL
        print("--" * 20)
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






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

 #ENTRADA DE DADOS
P1 = float(input("Digite a nota da  1° Prova: "))
P2 = float(input("Digite a nota do  2° Prova: "))

#PROCESSAMENTO
s = P1 * 1 + P2 * 2
media = s / 3
    
#ESTRUTURAIS CONDICIONAIS
print("--" * 20)
if media >= 6 :
    print(f"Aluno (APROVADO) com média: {media:.2f}")
    print("--" * 20)
    sleep(2)
else:
    print(f"Aluno (REPROVADO) com média: {media:.2f}")   
    print("--" * 20)
    sleep(2)

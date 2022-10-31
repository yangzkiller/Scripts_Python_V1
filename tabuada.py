#TABUADA 
#DATA: 09/05/22
#PROGRAMADOR: YANGZ
#CABECALHO

#BIBLIOTECA DE CONTROLE DE TEMPO
from time import sleep

#LIMPAR
def limpar():
    print("\n" * 100)

#CABEÇALHO
def cabecalho():
    print("-=" *20)
    print("{:^40}".format("TABUADA"))
    print('-=' *20)

#TABUADA
def tabuada():
    #LAÇO Principal
    while True:
        #ENTRADA DE DADOS
        n = int(input('Quer ver a tabuada de qual valor: '))
        print('=-' *20)
        #ESTRUTURA BREAK
        if n < 0:
            break
        #CONTADOR
        for c in range(1, 11):
            print(f'{n} x {c} = {n*c}') 
        print('=-' *20)   
    print('PROGRAMA TABUADA ENCERRADO')

#EXECUÇÃO
limpar()
cabecalho()
tabuada()

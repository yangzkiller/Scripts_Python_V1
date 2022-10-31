#TABUADA 
#DATA: 09/05/22
#PROGRAMADOR: YANGZ
#CABECALHO

#BIBLIOTECA DE CONTROLE DE TEMPO
from time import sleep

#TERMINAL COLOR
reset = '\033[37m'
red = '\033[91m'
green = '\033[92m'
yellow = '\033[93m'
blue = '\033[94m'

#LIMPAR
def limpar():
    print("\n" * 100)

#CABEÇALHO
def cabecalho():
    print(red,"-=" *20)
    print(yellow,"{:^40}".format("TABUADA"))
    print(red,'-=' *20,yellow)

#TABUADA
def tabuada():
    #LAÇO PRINCIPAL
    while True:
        #ENTRADA DE DADOS
        n = int(input('Quer ver a tabuada de qual valor: '))
        print(red,'=-' *20)
        #ESTRUTURA BREAK
        if n < 1:
            break
        #CONTADOR
        for c in range(1, 11):
            print(yellow, f'{n} x {c} = ',green,f'{n*c}') 
        print(red,'=-' *20,yellow)   
    print('PROGRAMA TABUADA ENCERRADO')

#EXECUÇÃO
limpar()
cabecalho()
tabuada()

#CALCULATOR
#DATA: 12/05/22
#PROGRAMADOR: YANGZ
#ALTERAÇÃO: 19/08/2022

#CORES TERMINAL
reset = '\033[1;37m'
red = '\033[1;31m'
green = '\033[1;32m'
blue = '\033[1;34m'
purple = '\033[1;35m'
yellow = '\033[1;33m'

#INICIALIZAÇÃO
from time import sleep
print(green,'=-' *20)
print(blue,"{:^40}".format("CALCULADORA"))
print(green,'=-' *20 ,purple)
(sleep(1.5))

#PRIMEIRA ENTRADA DE DADOS
n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
print(green,'=-' *20)
(sleep(1.5))

#LAYOUT
opcao = 0
while opcao != 7:
    print(green,"[ 1 ]",blue,"Somar")
    print(green,"[ 2 ]",blue,"Subtrair")
    print(green,"[ 3 ]",blue,"Multiplicar")
    print(green,"[ 4 ]",blue,"Dividir")
    print(green,"[ 5 ]",blue,"Maior")
    print(green,"[ 6 ]",blue,"Novos Números")
    print(green,"[ 7 ]",red,"Sair do Programa")
  
    print(green,'=-' *20 ,purple)
    opcao = int(input(' SELECIONE UMA OPÇÃO: '))

#SOMA
    if opcao == 1:
        soma = n1 + n2
        print(blue,f'A SOMA ENTRE',yellow,f'{n1} + {n2}:',green,f'{soma}')
        print(green,'=-' *20)
        (sleep(2))
#SUBTRAIR
    elif opcao == 2:
        subtrair = n1 - n2
        print(blue,f'SUBTRAÇÃO ENTRE',yellow,f'{n1} - {n2}:',green,f'{subtrair}')
        print(green,'=-' *20)
        (sleep(2))
#MULTIPLICAR
    elif opcao == 3:
        multiplicar = n1 * n2
        print(blue,f'A MULTIPLICAÇÃO ENTRE',yellow,f'{n1} . {n2}:',green,f'{multiplicar}')
        print(green,'=-' *20)
        (sleep(2))
#DIVIDIR
    elif opcao == 4:
        dividir = n1 / n2
        print(blue,f'A DIVISÃO ENTRE',yellow,f'{n1} / {n2}:',green,f'{dividir}')
        print(green,'=-' *20)
        (sleep(2))
#MAIOR
    elif opcao == 5:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(blue,f'ENTRE',yellow,f'{n1}',blue,f'E',yellow,f'{n2}',blue,f'O MAIOR VALOR É:',green,f'{maior}')
        print(green,'=-' *20)
        (sleep(2))
#NOVOS NÚMEROS
    elif opcao == 6:
        print(blue,'INFORME OS NÚMEROS NOVAMENTE: ')
        print(green,'=-' *20,purple)
        (sleep(2))
        n1 = int(input('PRIMEIRO VALOR: '))
        n2 = int(input('SEGUNDO VALOR: '))
#SAIR DO PROGRAMA
    elif opcao == 7:
        print(red,'FINALIZANDO...')
        print(green,'=-' *20)
        (sleep(1))
#INVÁLIDO
    else:
        print(red,'OPÇÃO INVÁLIDA... TENTE NOVAMENTE')
        print(green,'=-' *20)
        (sleep(2))
print(red,'FIM DO PROGRAMA')
print(green,'=-' *20)
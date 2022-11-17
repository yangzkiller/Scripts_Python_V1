#CAIXA ELETRONICO
#PROGRAMADOR: YANGZ
#ALTERAÇÃO: 19/08/22

#CORES TERMINAL
reset = '\033[1;00m'
red = '\033[1;31m'
green = '\033[1;32m'

#LAYOUT E ENTRADA DE DADOS
print('=' * 30)
print(red, '{:^30}'.format('BANCO 123'))
print(reset, '=' * 30 ,red)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
céd = 200
totcéd = 0

#ESTRUTURAS DE CONDIÇÃO
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(green, f'Total de {totcéd} cédulas de R${céd}')
        if céd == 200:
            céd = 100
        elif céd == 100:
            céd = 50
        elif céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 5
        elif céd == 5:
            céd = 1
        totcéd = 0
        if total == 0:
            break

#LAYOUT      
print(reset, '=' * 30)
print(red, 'Volte sempre ao BANCO 123: Tenha um bom dia!')
print(reset, '=' * 30)
#CADASTRO TRABALHADOR
#PROGRAMADOR: YANGZ
#DATA: 04/09/22

from time import sleep
#IMPORTA HORARIO DO COMPUTADOR
from datetime import datetime

#LAYOUT
print('==' *30)
print('              |CADASTRO DE FUNCIONÁRIO|')
print('==' *30)
sleep(1)

#ENTRADA DE DADOS
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input("Ano de Nascimento: "))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira d Trabalho (0 não tem): '))

#CONDIÇÃO
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=' *30)

#LAÇO
for k, v in dados.items():
    print(f'  -> {k}: {v}')
print('==' *30)

#GERADOR DE SENHAS
#DATA:18/08/2022
#PROGRAMADOR: YANGZ

#CORES TERMINAL
reset = '\033[1;30m'
red = '\033[1;31m'
blue = '\033[1;34m'
purple = '\033[1;35m'

from random import choice
import string
from time import sleep

#LAYOUT
print(red,'-=' *20)
print(purple,'          |GERADOR DE SENHA|')
print(red,'-=' *20,blue)
sleep(1)

#ENTRADA DE DADOS, CHAMADA DAS IMPORTAÇÕES
tamanho_senha = int(input('QUANTOS DIGITOS VOCE QUER NA SUA SENHA: '))
caracteres = string.ascii_letters + string.digits + string.punctuation
senha_segura = ''

#LAÇO
for i in range(tamanho_senha):
    senha_segura += choice(caracteres)

#LAYOUT
sleep(1)
print(purple,'...LOADING...')
sleep(1)
print(red,'-=' *20)
print(blue,'A SENHA (SEGURA) GERADA É:\033[1;92m ',senha_segura)
print(red,'-=' *20)
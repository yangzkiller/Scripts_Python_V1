#IMC
#PROGRAMADOR: YANGZ
#DATA: 09/05/22

#V1 - Programa que calcula o IMC de uma pessoa

#VARIAVEIS
print('-=' *20)
peso =  float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
print('-=' *20)
imc = peso / (altura ** 2)

#ESTRUTURA CONDICIONAL
print('O IMC desta pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce está ABAIXO DO PESO normal')
elif 18.6 <= imc < 25:
    print('Voce está no PESO IDEAL')
elif 25 <= imc < 30:
    print('Voce está com SOBREPESO')
elif 30 <= imc < 35:
    print('Voce está com OBESIDADE GRAU I')
elif 35 <= imc < 40:
    print('Voce está com OBESIDADE GRAU II (severa)')
else:
    print('Voce está com OBESIDADE GRAU III (mórbida)')
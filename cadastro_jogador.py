#CADASTRO DE JOGADOR
#PROGRAMADOR: YANGZ
#DATA: 06/09/22

#TERMINAL COLOR
reset = '\033[1;37m'
red = '\033[1;31m'
green = '\033[1;32m'
blue = '\033[1;34m'
purple = '\033[1;35m'
yellow = '\033[1;33m'

#VARIAVEIS
time = list()
jogador = dict()
partidas = list()

#LAÇO PRINCIPAL
while True:
    jogador.clear() #limpa a tela para receber dados novos
    print(red, '-=' *30 ,reset)
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    print(red, '-' *30 ,reset)
    partidas.clear()
    #CONTADOR
    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na partida {c+1}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    print(red, '-' *30 ,yellow)

    #LAÇO PRA SABER SE QUER PROSEGUIR
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print(red, 'ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

#RESULTADOS
#CABEÇALHO
print(red, '-=' *30)
print(green, 'cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
#LAYOUT TABELA
print(red, '-' *40 ,reset)
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f' {str(d):<15}', end='')
    print()
print(red, '-' *40 ,red)

#CHAVE DE BUSCA
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(red, f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(green, f' --> LEVANTAMENTO DO JOGADOR: {time[busca]["nome"]}',reset)
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print(red, '-' *40)
print(green, '<< VOLTE SEMPRE >>')


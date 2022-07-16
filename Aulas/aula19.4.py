desempenhoJogador = {}
jogadores = []
while True:
    desempenhoJogador["Nome"] = str(input('Digite o nome do jogador: '))
    desempenhoJogador["Partidas"] = int(input('Digite quantas partidas esse jogador participou: '))
    desempenhoJogador["Gols"] = int(input('Digite quantos gols esse jogador fez nas partidas: '))
    desempenhoJogador["Assistencias"] = int(input('Digite quantas assistências esse jogador teve: '))
    desempenhoJogador["Desempenho"] = (desempenhoJogador["Gols"] + desempenhoJogador["Assistencias"]) / desempenhoJogador["Partidas"]
    jogadores.append(desempenhoJogador.copy())
    desempenhoJogador.clear()
    r = str(input('Deseja continuar? [S/N]: '))
    if r in 'Ss':
        jogadores = jogadores
    elif r in 'Nn':
        break
    else:
        print('Resposta inválida! ')
for c in jogadores:
    print('-=' * 30)
    for k, v in c.items():
        if k == "Desempenho":
            print(f'O {k} do jogador é de {v:.1f} participações por partida. ')
        elif k == "Nome":
            print(f'O {k} do jogador é {v}')
        else:
            print(f'O No de {k} é: {v}')

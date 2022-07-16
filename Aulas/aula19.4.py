desempenhoJogador = {}
jogadores = []
while True:
    desempenhoJogador["Nome"] = str(input('Digite o nome do jogador: '))
    desempenhoJogador["Partidas"] = int(input('Digite quantas partidas esse jogador participou: '))
    desempenhoJogador["Gols"] = int(input('Digite quantos gols esse jogador fez nas partidas: '))
    desempenhoJogador["Assistencias"] = int(input('Digite quantas assistências esse jogador teve: '))
    jogadores.append(desempenhoJogador.copy())
    desempenhoJogador.clear()
    r = str(input('Deseja continuar? [S/N]: '))
    if r in 'Ss':
        jogadores = jogadores
    elif r in 'Nn':
        break
    else:
        print('Resposta inválida! ')


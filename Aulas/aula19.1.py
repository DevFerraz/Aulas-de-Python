from random import randint
from operator import itemgetter
jogadores = {}
total = []
for c in range(0, 4):
    jogadores["Jogador"] = str(input('Digite o nome do jogador: '))
    jogadores["Valor"] = randint(1, 6)
    total.append(jogadores.copy())
    jogadores.clear()
ranking = []
for c in total:
    for d, v in c.items():
        print(f'{d}: {v} ')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for d, v in enumerate(ranking):
    print(f'O {d} lugar é do jogador {v[0]} que tirou {v[1]} ')
#for c, d in ranking:
#    if d[c][1] in ranking == d[c+1][1]:
#        print('Aconteceu um empate! Tente novamente!')
#        break

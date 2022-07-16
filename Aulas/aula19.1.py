from random import randint
total = {}
jogadores = []
for c in range(0, 4):
    total["Jogador"] = str(input('Digite o nome do jogador: '))
    total["Valor"] = randint(1, 6)
    jogadores.append(total.copy())
for c, v in enumerate(jogadores):
    print(f'O jogador {jogadores["Jogador"][v]} tirou {jogadores["Valor"][v]}. ')
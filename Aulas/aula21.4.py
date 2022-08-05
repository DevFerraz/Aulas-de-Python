def ficha(nome='', gols=''):
    """
    Cria uma ficha de um jogador com seu desempenho de gols.
    :param nome: Nome do jogador
    :param gols: Quantidade de gols feitos pelo jogador
    :return: sem return
    """
    if nome == '':
        print(f'Jogador não definido fez {gols} gols. ', end='')
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    if nome != '':
        print(f'O jogador {nome} fez {gols} gols')


r1 = str(input('Digite o nome do jogador: '))
r2 = str(input('Digite quantos gols ele fez: '))
ficha(r1, r2)


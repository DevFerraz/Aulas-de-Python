def ficha(nome='', gols=''):
    """
    Cria uma ficha de um jogador com seu desempenho de gols.
    :param nome: Nome do jogador
    :param gols: Quantidade de gols feitos pelo jogador
    :return: sem return
    """
    if nome == '':
        print('Jogador não definido', end='')
    if gols == 0 or gols == str:
        print('Fez 0 gols')
    if nome != '' and gols != 0 and gols in str:
        print(f'O jogador {nome} fez {gols} gols')


r1 = input('Digite o nome do jogador: ')
r2 = input('Digite quantos gols ele fez: ')
ficha(r1, r2)


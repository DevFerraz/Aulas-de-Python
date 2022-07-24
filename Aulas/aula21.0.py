def contador(i, f, p):
    """
    --> Faz uma contagem na tela com 3 parâmetros
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM! ')


contador(1, 7, 0.5)
help(contador)

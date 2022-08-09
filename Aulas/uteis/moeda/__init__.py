def dobro_moeda(n):
    if n == -1:
        return 'Número inválido!'
    return n * 2


def metade_moeda(n):
    if n == -1:
        return 'Número inválido!'
    return n / 2


def aumentar_moeda(n, p):
    if n == -1:
        return 'Número inválido!'
    return n + n * p / 100


def diminuir_moeda(n, p):
    if n == -1:
        return 'Número inválido!'
    return n - n * p / 100

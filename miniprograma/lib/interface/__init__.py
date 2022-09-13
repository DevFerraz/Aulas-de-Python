def leiaInt (msg):
    while True:
        try:
            n = int(input(msg))
        except Exception as error:
            print(f'\033[31mDigite um número inteiro válido! Erro {error.__class__}\033[m')
            continue
        else:
            return n


def linha(tam=30):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(30))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[35mEscolha uma opção: \033[m')
    return opc

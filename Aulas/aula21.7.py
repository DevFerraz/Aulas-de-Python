import time


cores = ('\033[m', # 0 - sem cor
         '\033[0;30;41m', # 1 - Vermelho
         '\033[0;30;42m',  # 2 - Verde
         '\033[0;30;43m',  # 3 - Amarelo
         '\033[0;30;44m',  # 4 - Azul
         '\033[0;30;45m',  # 5 - Roxo
         '\033[7;30m',  # 6 - Branco
         )


def ajuda(com):
    titulo(f'Acessando o manual do comando... \'{com}\'', 4)
    time.sleep(1.5)
    print(cores[6], end='')
    help(com)
    print(cores[0], end='')


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('=' * tam)
    print(f'  {msg}')
    print('=' * tam)
    print(cores[0], end='')


comando = ''
while True:
    titulo('Sistema de Ajuda PyHelp', 2)
    time.sleep(1)
    comando = str(input('Função ou biblioteca > '))
    time.sleep(0.4)
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até Logo!', 1)

def fatorial(n=0, show=''):
    f = 1
    print('Os números gerados na progressão foram:')
    for c in range(n, 0, -1):
        f *= c
        if show in 'Ss':
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
                print(f)
                print()
        elif show in 'Nn':
            print(f, end='')


def fatorial1():
    fator1 = int(input('Digite o número que deseja saber o fatorial: '))
    fator2 = str(input('Deseja saber os números gerados na progressão? '))
    fatorial(fator1, fator2)


fatorial1()
while True:
    r = str(input('Deseja continuar? [S/N] '))
    if r in 'Nn':
        break
    elif r in 'Ss':
        fatorial1()
    else:
        print('Resposta inválida! Tente novamente.')


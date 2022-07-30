def fatorial(n=0, show='n'):
    f = 1
    c1 = 0
    print('Os números gerados na progressão foram:')
    for c in range(n, 0, -1):
        f *= c
        c1 += 1
        if show in 'Nn':
            return f
        elif show in 'Ss':
            print(f'{f}')
        else:
            return 0
    return f


while True:
    fator1 = int(input('Digite o número que deseja saber o fatorial: '))
    fator2 = str(input('Deseja saber os números gerados na progressão? '))
    fatorial(fator1, fator2)
    while True:
        r = str(input('Deseja continuar? [S/N] '))
        if r in 'Nn':
            break
        elif r in 'Ss':
            r = r
        else:
            print('Resposta inválida! Tente novamente.')
    if r in 'Nn':
        break

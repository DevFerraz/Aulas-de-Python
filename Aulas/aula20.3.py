nrs = []


def maior(*num):
    nrs2 = num
    print(f'A lista dos números é essa:\n{num}')
    print(f'O maior número digitado foi: {max(nrs2)}')
    print(f'O menor número digitado foi {min(nrs2)}')


def loop():
    while True:
        t = int(input('Digite um número inteiro: '))
        if t >= 0:
            t = t
            nrs.append(t)
            break
        elif t <= 0:
            t = t
            nrs.append(t)
            break
        else:
            print('Resposta inválida! Tente novamente! ')


def loop2():
    while True:
        r = str(input('Deseja continuar? [S/N]: '))
        if r in 'Ss':
            loop()
        elif r in 'Nn':
            break
        else:
            print('Resposta inválida. Tente novamente! ')


loop()
loop2()
maior(nrs)



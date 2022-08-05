def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Você não digitou um número válido, tente novamente!')
        if ok:
            break
    return valor


n = leiaInt('Digite um número inteiro: ')
print(f'Você digitou o número {n}')

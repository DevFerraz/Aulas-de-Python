import time


def linha():
    print()
    print('-=' * 20)


def contador(a, b, c):
    linha()
    for d in range(a, b, c):
        print(d, end=' ')
        time.sleep(1)


def loop():
    while True:
        num1 = int(input('Digite de onde quer começar a contagem: '))
        num2 = int(input('Digite agora onde quer terminar sua contagem: '))
        if num2 > num1:
            num2 += 1
        elif num2 < num1:
            num2 -= 1
        num3 = int(input('Agora digite como quer que a contagem aconteça: '))
        if num1 > num2 and num3 > 0:
            num3 = num3 * -1
        print('PREPARANDO SUA CONTAGEM...')
        time.sleep(1.7)
        print('Vai ficar assim: ')
        time.sleep(1)
        contador(num1, num2, num3)
        print()
        break


linha()
print('Contando de 1 a 10 temos: ')
contador(1, 11, 1)
linha()
print('Contando regressivamente, de 10 a 0, temos: ')
contador(10, -1, -2)
linha()
print('Agora é sua vez! ')
loop()
while True:
    r = str(input('Quer fazer outra contagem? [S/N]: '))
    if r in 'Ss':
        loop()
    elif r in 'Nn':
        break
    else:
        print('Resposta invállida! Tente novamente! ')
print('Obrigado por jogar! ')

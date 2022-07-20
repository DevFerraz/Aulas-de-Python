import time


def linha():
    print()
    print('-=' * 20)


def contador(a, b, c):
    for d in range(a, b, c):
        print(d, end=' ')
        time.sleep(0.5)


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
        print(f'A contagem de {num1} até {num2} com razão {num3} vai ficar assim:')
        time.sleep(2.5)
        contador(num1, num2, num3)
        print()
        break


print('-=' * 20)
print('Contando de 1 a 10 temos: ')
print('-=' * 20)
time.sleep(2.5)
contador(1, 11, 1)
print()
print('Contando regressivamente, de 10 a 0, temos: ')
time.sleep(2.5)
contador(10, -1, -2)
print()
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

num = int(input('Digite um numero inteiro qualquer maior do que 0: '))
div = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end='')
        div += 1
    else:
        print('\033[31m', end='')
    print('{} ' .format(c), end='')
if div == 2:
    print('\n\33[mEste numero foi divisivel apenas {} vezes, logo, eh um numero primo! ' .format(div))
else:
    print('\n\33[mEste numero foi divisivel {} vezes, logo, nao eh um numero primo! ' .format(div))

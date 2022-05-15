num = int(input('Escreva um numero inteiro: '))
num2 = int(input('Escolha (1) para base binaria, (2) para octal e (3) para hexadecimal: '))
if num2 == int('1'):
    print('{} em binario eh: {}' .format(num, bin(num)[2:]))
elif num2 == int('2'):
    print('{} em octal eh: {}'.format(num, oct(num)[2:]))
elif num2 == int('3'):
    print('{} em hexadecimal eh: {}' .format(num, hex(num)[2:]))
else:
    print('Voce digitou uma opcao invalida!')
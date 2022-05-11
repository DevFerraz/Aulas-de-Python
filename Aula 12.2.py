num = int(input('Escreva um numero inteiro: '))
num2 = int(input('Escolha (1) para base binaria, (2) para octal e (3) para hexadecimal: '))
if num2 == int('1'):
    print(bin(num))
elif num2 == int('2'):
    print(oct(num))
elif num2 == int('3'):
    print(hex(num))
else:
    print('Voce digitou uma opcao invalida!')
n = float(input('Digite seu salario atual: R$'))
n1 = n * 1.1
n2 = n * 1.15
if n > 1250:
    print('Seu salario sera de: R${:.2f}' .format(n1))
else:
    print('Seu salario sera de: R${:.2f}' .format(n2))

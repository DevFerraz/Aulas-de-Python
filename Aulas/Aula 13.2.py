soma = 0
cont = 0
for contagem in range(3, 498, 3):
    if contagem % 2 != 0:
        cont = cont + 1
        print('{} + {}' .format(soma, contagem))
        soma = soma + contagem

print('A soma dos numeros eh: {} e a quantidade dos numeros eh: {}' .format(soma, cont))
soma = 0
for contagem in range(3, 498, 3):
    if contagem % 2 != 0:
        print('{} + {}' .format(soma, contagem))
        soma = soma + contagem

print(soma)
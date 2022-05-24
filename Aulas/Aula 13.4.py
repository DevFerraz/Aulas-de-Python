soma = 0
for c in range(0, 6):
    num = int(input('Digite um numero inteiro: '))
    if num % 2 == 0:
        soma += num
print('A soma dos numeros pares eh igual a: {}'.format(soma))
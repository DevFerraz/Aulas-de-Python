num = int(input('Digite um numero inteiro qualquer maior do que 0: '))
condicao = 1
memoria = 0
for c in range(1, num):
    if num % condicao == 0:
        memoria = condicao
        if memoria > 1 or memoria < num:
            print('Este numero nao eh primo! ')
        else:
            print('Este eh um numero primo! ')
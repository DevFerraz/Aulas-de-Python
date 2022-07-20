import random
import time

listPar = 0
num = int(input('Digite a quantidade de números que deseja sortear: '))


def sort(lista):
    print(f'Sorteando {num} valores da lista... ')
    time.sleep(2)
    print('A lista total de números sorteados é igual a: ')
    for e in range(0, num):
        n = random.randint(1, 100)
        lista.append(n)
        print(n, end=' ')
        time.sleep(1)
    print('\nPRONTO! ')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma de todos os valores pares sorteados é igual a {soma}')


lst = []
sort(lst)
somaPar(lst)


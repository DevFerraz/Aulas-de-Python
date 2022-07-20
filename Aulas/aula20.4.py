import random
import time

listPar = 0
lista = []


def sort():
    for e in range(0, 5):
        r = random.randint(1, 100)
        lista.append(r)


def somaPar():
    dado = 0
    for d, v in enumerate(lista):
        if v % 2 == 0:
            dado += v
        listPar = dado


sort()
somaPar()
print('A lista total de números sorteados é igual a: ')
for c, f in enumerate(lista):
    print(f, end=' ')
    time.sleep(1)
    print()
print(f'A soma do total de números pares da lista é igual a {}')

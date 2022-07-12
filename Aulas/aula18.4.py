from random import randint
import time
total = []
jogosFinais = []
quant = int(input('Quantos jogos você quer jogar? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in total:
            total.append(num)
            cont += 1
        if cont >= 6:
            break
    total.sort()
    jogosFinais.append(total[:])
    total.clear()
    tot += 1
print('=-' * 5, f'SORTEANDO {quant} JOGOS', '=-' * 5)
time.sleep(1.5)
for c, v in enumerate(jogosFinais):
    print(f'O {c+1}o. jogo é: {v} ')
    time.sleep(1)
print('=-' * 7, 'BOA SORTE!', '=-' * 6)

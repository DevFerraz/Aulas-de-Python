import random
import time
n = int(random.uniform(1, 10)) #pode utilizar tambem randint, eh mais facil#
n1 = int(input('Digite um numero inteiro de 1 a 10: '))
print('PROCESSANDO...')
time.sleep(2)
if n == n1:
    print('Parabens! Voce acertou o numero e ganhou o jogo!')
else:
    print('Voce errou! Eu pensei em {}! Tente novamente! ' .format(n))



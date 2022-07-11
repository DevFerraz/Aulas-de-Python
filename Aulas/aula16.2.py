import random
num = (random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100))
print(f'Os valores sorteados foram: {num}')
print('O maior número gerado é: {}'.format(max(num)))
print(f'O menor numero gerado é: {min(num)}')
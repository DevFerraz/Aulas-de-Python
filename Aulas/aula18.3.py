matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = 0
for a in range(0, 3):
    for c in range(0, 3):
        matriz[a][c] = int(input(f'Digite o valor [{a}], [{c}]: '))
print(f'[{matriz [0][0]:^5}] [{matriz[0][1]:^5}] [{matriz[0][2]:^5}]')
print(f'[{matriz [1][0]:^5}] [{matriz[1][1]:^5}] [{matriz[1][2]:^5}]')
print(f'[{matriz [2][0]:^5}] [{matriz[2][1]:^5}] [{matriz[2][2]:^5}]')
for c, v in enumerate(matriz[0]):
    if v % 2 == 0:
        par += v
for c, v in enumerate(matriz[1]):
    if v % 2 == 0:
        par += v
for c, v in enumerate(matriz[2]):
    if v % 2 == 0:
        par += v
soma = matriz[0][1] + matriz[1][1] + matriz[2][1]
maior = 0
for c, v in enumerate(matriz[1]):
    if v > maior:
        maior = v
print(f'A soma dos valores pares é: {par}')
print(f'A soma dos valores da segunda coluna é igual a: {soma}')
print(f'O maior valor encontrado na seguna linha é {maior}')


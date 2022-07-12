valores = []
impar = []
par = []
for c in range(0, 7):
    valores.append(int(input(f'Digite o {c+1} valor inteiro: ')))
for c, v in enumerate(valores):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
par.sort()
impar.sort()
print(f'Os valores pares em ordem crescente são: {par}')
print(f'Os valores ímpares em ordem crescente são: {impar}')

# valores = [[], []]
# valor = 0
# for c in range(0, 7)
# valor = int(input(f'Digite o {c}o. valor: '))
# if valor % 2 == 0
#       valores[0].append(valor)
# else:
#       valores[1].append(valor)
# valores[0].sort()
# valores[1].sort
# print(f'Os valores pares em ordem crescente são: {valores[0]}')
# print(f'Os valores ímpares em ordem crescente são: {valores[1]}')

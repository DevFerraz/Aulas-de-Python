lista = []
listaPar = []
listaImpar = []
while True:
    lista.append(int(input('Digite um número inteiro: ')))
    resposta = str(input('Deseja continuar? '))
    if resposta in 'Nn':
        break
    if resposta in 'Ss':
        lista = lista
    else:
        print('Resposta inválida! ')
for c, v in enumerate(lista):
    if v % 2 == 0:
        listaPar.append(v)
    elif v % 2 == 1:
        listaImpar.append(v)
print(f'A lista completa é: {lista}')
lista.sort()
listaPar.sort()
listaImpar.sort()
print(f'Ordenada de forma crescente fica assim: {lista}')
print(f'A lista de pares, ordenada de forma crescente é: {listaPar}')
print(f'A lista de ímpares ordenada de forma crescente é: {listaImpar}')

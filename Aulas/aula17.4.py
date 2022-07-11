lista = []
listaPar = []
listaImpar = []
while True:
    lista.append(int(input('Digite um número inteiro: ')))
    resposta = str(input('Deseja continuar? '))
    if resposta in 'Nn':
        break
    if resposta in 'Ss':
        lista == lista
    else:
        print('Resposta inválida! ')
for c in range(0, len(lista)):
    if c % 2 == 0:
        listaPar.append(lista.index(c))
    elif c % 2 == 1:
        listaImpar.append(lista.index(c))
print(f'A lista completa é: {lista}')
print(f'A lista de pares é {listaPar}')
print(f'A lista de ímpares é {listaImpar}')

lista = []
listaPar = []
listaImpar = []
num = int(input('Digite um número inteiro: '))
lista.append(num)
resposta = ''
while True:
    resposta = input(print('Deseja continuar? ')).upper()
    if resposta == 'S':
        num = int(input('Digite um número inteiro: '))
        lista.append(num)
    else:
        break
for c in range(0, len(lista)):
    if c % 2 == 0:
        listaPar.append(lista.index(c))
    elif c % 2 == 1:
        listaImpar.append(lista.index(c))
print(f'A lista completa é: {lista}')
print(f'A lista de pares é {listaPar}')
print(f'A lista de ímpares é {listaImpar}')

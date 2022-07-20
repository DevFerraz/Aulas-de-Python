lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
    if r in 'Ss':
        lista = lista
    else:
        print('Resposta inválida! ')
lista.sort(reverse=True)
print(f'A quantidade de elementos na lista foi de: {len(lista)}')
print(f'A lista em ordem decrescente fica assim: {lista}')
if 5 in lista:
    print(f'O valor 5 esta na posição {lista.index(5)} da lista')
else:
    print('O valor 5 não foi encontrado na sua lista! ')
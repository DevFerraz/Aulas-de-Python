lista = []
num = 0
while num != 999:
    num = int(input('Digite um valor inteiro (Digite [999] para terminar.):'))
    if num in lista:
        lista = lista
    elif num == 999:
        lista = lista
    else:
        lista.append(num)
lista.sort()
print(f'Os valores em ordem crescente ficam assim: {lista}')

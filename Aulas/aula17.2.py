lista = []
for c in range (0, 5):
    num = int(input('Digite um número: '))
    lista.append(num)
for c in range(lista):
    if lista[c] > lista[c+1]:
        lista == lista
    elif lista[c] < lista[c+1]:
        lista[c] = lista[c+1]
print(lista)
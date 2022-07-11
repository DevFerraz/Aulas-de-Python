lista = []
for c in range (0, 5):
    num = int(input('Digite um valor: '))
    lista.append(num)
print(f'O maior valor digitado foi {max(lista)}! ')
print(f'O menor valor digitado foi {min(lista)}! ')
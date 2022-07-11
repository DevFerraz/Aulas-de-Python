lista = []
num = int(input('Digite um número: '))
lista.append(num)
while True:
    r = input('Quer continuar? [S/N]: ')
    if r == 'S' or r =='s':
        num = int(input('Digite um número: '))
        lista.append(num)
    else:
        break
print(f'A quantidade de números digitados foi {len(lista)}')
print(f'A lista em ordem decrescente fica: {lista.sort(reverse = True)}')
if 5 in lista:
    print(f'O valor 5 foi digitado na posição {lista.index(5)} da lista')
else:
    print('O valor 5 nào foi digitado nessa lista. ')
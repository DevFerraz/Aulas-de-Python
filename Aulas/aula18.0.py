total = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(float(input('Digite o peso: ')))
    if len(total) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    resposta = str(input('Quer continuar? [S/N]: '))
    total.append(dados[:])
    dados.clear()
    if resposta in 'Nn':
        break
    elif resposta in 'Ss':
        total = total
    else:
        print('Resposta inválida! ')
print(f'A quantidade de pessoas na lista é de: {len(total)}')
total.sort()
for p in total:
    if p[1] == maior:
        print(f'O maior peso foi de {p[0]}, com {maior}kg! ')
for p in total:
    if p[1] == menor:
        print(f'O menor peso foi de {p[0]}, com {menor}kg! ')

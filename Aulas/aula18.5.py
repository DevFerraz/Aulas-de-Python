completa = []
dados = []
medias = []
while True:
    dados.append(str(input('Digite o nome do aluno: ')))
    n1 = float(input('Digite a primeira nota do aluno: '))
    n2 = float(input('Digite a segunda nota do aluno: '))
    m = (n1 + n2) / 2
    dados.append(n1)
    dados.append(n2)
    medias.append(m)
    completa.append(dados[:])
    dados.clear()
    r = str(input('Deseja cadastrar outro aluno? [S/N] '))
    if r in 'Ss':
        completa == completa
    elif r in 'Nn':
        break
    else:
        print('Resposta inválida! ')
for c, v in enumerate(medias):
    print(f'A média do {c+1} aluno é {v}')
    if 6 < v <= 10:
        print('O aluno foi aprovado.')
    elif 0 < v < 6:
        print('O aluno está reprovado. ')
    else:
        print('A nota da média é inválida. ')
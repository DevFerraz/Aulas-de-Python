aluno = {}
total = []
while True:
    aluno['Nome'] = str(input('Digite o nome do aluno: '))
    aluno['Nota'] = float(input('Digite a nota final do aluno: '))
    if aluno['Nota'] >= 7:
        aluno['Situacao'] = 'Aprovado'
    elif 5 <= aluno['Nota'] < 7:
        aluno['Situacao'] = 'Recuperação'
    else:
        aluno['Situacao'] = 'Reprovado'
    total.append(aluno.copy())
    aluno.clear()
    r = str(input('Deseja continuar? [S/N] '))
    if r in 'Nn':
        break
    elif r in 'Ss':
        r = r
    else:
        print('Resposta inválida! ')
print('A relação dos alunos aprovados é: ')
for c in total:
    for k, v in c.items():
        print('-=' * 15)
        print(f'{k:^10} é {v:^10}')


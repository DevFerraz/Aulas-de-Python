aluno = {}
total = []
while True:
    aluno['Nome'] = str(input('Digite o nome do aluno: '))
    aluno['Nota'] = float(input('Digite a nota final do aluno: '))
    if aluno['Nota'] >= 7:
        aluno['Situacao'] = 'Aprovado'
    else:
        aluno['Situacao'] = 'Reprovado'
    total.append(aluno.copy())
    r = str(input('Deseja continuar? [S/N] '))
    if r in 'Nn':
        break
    elif r in 'Ss':
        r = r
    else:
        print('Resposta inválida! ')
print('A relação dos alunos aprovados é: ')
for c in total:
    for d, k in c.values():
        print(f'O aluno {d["Nome"][k]} está {d["Situacao"][k]} ')

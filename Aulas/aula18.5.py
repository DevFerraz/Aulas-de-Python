completa = []
while True:
    nome = (str(input('Digite o nome do aluno: ')))
    n1 = float(input('Digite a primeira nota do aluno: '))
    n2 = float(input('Digite a segunda nota do aluno: '))
    m = (n1 + n2) / 2
    completa.append([nome, [n1, n2], m])
    if m < 0:
        print('Notas inválidas! ')
        completa.pop()
    elif m > 10:
        print('Notas inválidas! ')
        completa.pop()
    r = str(input('Deseja cadastrar outro aluno? [S/N] '))
    if r in 'Ss':
        completa = completa
    elif r in 'Nn':
        break
    else:
        print('Resposta inválida! ')
for c, v in enumerate(completa):
    print(f'{c+1:<4} A média do aluno {v[0]:<6} é {v[2]:>5.1f}')
while True:
    opc = int(input('Mostrar notas de qual aluno? (Digite 999 para sair): '))
    if opc == 999:
        break
    if opc <= len(completa):
        print(f'As notas de {completa[opc - 1][0]}, são: {completa[opc - 1][1]}')
    else:
        print('Opção inválida! ')
print('-=' * 7, 'Muito Obrigado! Até Logo!', '-=' * 7)

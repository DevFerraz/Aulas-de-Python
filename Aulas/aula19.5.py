pessoa = {}
total = []
while True:
    pessoa["Nome"] = str(input('Digite o nome da pessoa: '))
    pessoa["Sexo"] = str(input('Digite o sexo da pessoa [M/F]: '))
    if pessoa["Sexo"] in 'Mm':
        pessoa = pessoa
    elif pessoa["Sexo"] in 'Ff':
        pessoa = pessoa
    else:
        print('Resposta inválida')
        pessoa["Sexo"] = 'Indefinido'
    pessoa["Idade"] = int(input('Digite a idade da pessoa: '))
    total.append(pessoa.copy())
    pessoa.clear()
    r = str(input('Deseja continuar? [S/N]: '))
    if r in 'Ss':
        pessoa = pessoa
    elif r in 'Nn':
        break
    else:
        print('Resposta inválida! ')
mulheres = []
for c, v in enumerate(total):
    if 'Sexo' in 'Ff':
        mulheres = v
print(mulheres)





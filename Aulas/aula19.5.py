pessoa = {}
total = []
soma = media = 0
mulheres = []
while True:
    pessoa["Nome"] = str(input('Digite o nome da pessoa: '))
    while True:
        pessoa["Sexo"] = str(input('Digite o sexo da pessoa [M/F]: ')).upper()[0]
        if pessoa["Sexo"] in 'MF':
            break
        else:
            print('Resposta inválida')
    pessoa["Idade"] = int(input('Digite a idade da pessoa: '))
    soma += pessoa["Idade"]
    if pessoa["Sexo"] in 'F':
        mulheres.append(pessoa.copy())
    total.append(pessoa.copy())
    pessoa.clear()
    while True:
        r = str(input('Deseja continuar? [S/N]: ')).upper()[0]
        if r in 'SN':
            break
        else:
            print('Resposta inválida! ')
    if r == 'N':
        break
media = soma / len(total)
print(f'O total de pessoas cadastradas foi {len(total)}')
print(f'A média das idades é igual a {media:.2f}')
print('A lista de mulheres é: ')
for p in total:
    if p["Sexo"] == 'F':
        print(p["Nome"])
print('As pessoas acima da média foram:')
for p in total:
    if p["Idade"] > media:
        print(f'{p["Nome"]} com {p["Idade"]} anos. ')

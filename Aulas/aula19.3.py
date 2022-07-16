pessoa = {}
total = []
while True:
    pessoa["Nome"] = str(input('Digite o nome da pessoa: '))
    pessoa["Ano"] = int(input('Digite o ano de nascimento da pessoa: '))
    pessoa["CTPS"] = int(input('Digite o número de contratos da sua CTPS: '))
    if pessoa["CTPS"] > 0:
        pessoa["Contratacao"] = int(input('Digite o ano de contratação do primeiro emprego: '))
        pessoa["Salario"] = float(input('Digite o salário do respectivo emprego: '))
    if pessoa["CTPS"] < 0:
        print('Digite uma informação válida. ')
    if pessoa["CTPS"] == 0:
        print('Você ainda precisa começar a trabalhar! Até o momento, faltam 35 anos para sua aposentadoria! ')
        total.append(pessoa.copy())
        pessoa.clear()
    r = str(input('Deseja continuar? [S/N]: '))
    if r in 'Ss':
        total = total
    elif r in 'Nn':
        break
    else:
        print('Opção inválida! ')
print(total)

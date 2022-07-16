from datetime import datetime
anoAtual = datetime.now().year
pessoa = {}
total = []
while True:
    pessoa["Nome"] = str(input('Digite o nome da pessoa: '))
    pessoa["Ano"] = int(input('Digite o ano de nascimento da pessoa: '))
    if 1902 < pessoa["Ano"] < 1922:
        print('Tem certeza que você é tão velho? ^^')
    elif pessoa["Ano"] < 1902:
        print('Acho que essa pessoa já virou pó hein... Deus a tenha! XD ')
    elif pessoa["Ano"] > anoAtual:
        print('Essa pessoa ainda não nasceu! ')
        print('O processo foi encerrado devido à invalidade de informações. ')
        break
    pessoa["CTPS"] = int(input('Digite o número de contratos da sua CTPS: '))
    if pessoa["CTPS"] > 0:
        pessoa["Contratacao"] = int(input('Digite o ano de contratação do primeiro emprego: '))
        pessoa["Salario"] = float(input('Digite o salário do respectivo emprego: '))
    if pessoa["CTPS"] < 0:
        print('Digite uma informação válida. ')
        pessoa["CTPS"] = 0
    if pessoa["CTPS"] == 0:
        print('Você ainda precisa começar a trabalhar! Até o momento, faltam 35 anos para sua aposentadoria! ')
    pessoa["Aposentadoria"] = pessoa["Contratacao"] + 35
    total.append(pessoa.copy())
    pessoa.clear()
    r = str(input('Deseja continuar? [S/N]: '))
    if r in 'Ss':
        total = total
    elif r in 'Nn':
        break
    else:
        print('Opção inválida! ')
for c in total:
    for d, v in c.items():
        print('-=' * 25, '-')
        if d == "Aposentadoria":
            print(f'Sua {d:^5} será em {v:^5}! Faltam {v - anoAtual:^5} anos! ')
        else:
            print(f'{d:^15} é {v:^15}')

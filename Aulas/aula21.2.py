#from datetime import date
#ano atual -> date.today().year


def voto(nascimento):
    import datetime
    data = datetime.date.today()
    ano = int(data.strftime("%Y"))
    opcao = ano - nascimento
    if opcao < 16:
        return f'Voto NEGADO! {opcao} anos não é uma idade válida para voto!'
    elif 18 < opcao < 65:
        return f'Com {opcao} anos, o voto é OBRIGATÓRIO!'
    elif opcao > 120:
        return f'{opcao} anos?? Você existe?'
    elif opcao > 65 or 16 < opcao < 18:
        return f'Com {opcao} anos, o voto é OPCIONAL'


r1 = int(input('Digite o ano que você nasceu: '))
print(voto(r1))

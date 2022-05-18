from datetime import datetime
sexo = str(input('Digite "H" se voce for homem e "M" se voce for mulher: '))
if sexo == 'H' or sexo == 'h':
    nascimento = int(input('Digite o ano do seu nascimento: '))
    hoje = datetime.today().year
    idade = hoje - nascimento
    if idade < 18:
        diferenca1 = 18 - idade
        print('Ainda nao esta na hora de se alistar, ainda faltam {} anos! ' .format(diferenca1))
        print('Voce deve se alistar em {}! ' .format(hoje + diferenca1))
    elif idade > 18:
        diferenca2 = idade - 18
        print('Ja passaram {} anos da hora de se alistar! ' .format(diferenca2))
        print('Voce deveria ter se alistado em {}! ' .format(hoje - diferenca2))
    elif idade == 18:
        print('Eh hora de se alistar! ')
elif sexo == "M" or sexo == 'm':
    print('Por voce ser mulher, seu alistamento nao eh obrigatorio. ')
else:
    print('Opcao invalida!')


from datetime import datetime
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


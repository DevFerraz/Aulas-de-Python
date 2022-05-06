from datetime import date
ano = int(input('Qual ano voce quer analisar? Digite 0 se quiser analisar o ano atual: ').strip())
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} eh bissexto! ' .format(ano))
else:
    print('O ano de {} nao eh bissexto! ' .format(ano))
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    nasc = int(input("Em que ano nasceu a {}ª pessoa? " .format(c)))
    idade = atual - nasc
    print("A pessoa tem {} anos. " .format(idade))
    if idade >= 21:
        totmaior = totmaior + 1
    else:
        totmenor += 1
print("O total de pessoas maiores eh {} e de menores eh {}! " .format(totmaior, totmenor))

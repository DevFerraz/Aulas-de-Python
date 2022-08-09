import uteis

while True:
    num = str(input('Digite um valor inteiro: '))
    if num.isnumeric() > 0:
        num = int(num)
        break
    else:
        print('Opção inválida, tente novamente')
fat = uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {uteis.dobro(num)}')
print(f'O triplo de {num} é {uteis.triplo(num)}')

from uteis import moeda


def programa():
    while True:
        valor = str(input('Digite o valor da moeda que deseja: R$')).replace(',', '.')
        if valor.isalpha() or valor.strip() == '':
            valor = -1
        valor = float(valor)
        if valor == -1:
            print(moeda.dobro_moeda(valor))
            break
        print(f'O dobro do valor é: R${moeda.dobro_moeda(valor):.2f}')
        print(f'A metade do valor é: R${moeda.metade_moeda(valor):.2f}')
        while True:
            x = 0
            porcentagem = str(input('Digite uma porcentagem que deseja aumentar no valor inserido: ')).replace(',', '.')
            if porcentagem.isalpha():
                x = -1
            if x == -1:
                print('Valor inválido!')
            if x != -1:
                porcentagem = float(porcentagem)
                break
        print(f'O valor R${valor} com {porcentagem}% de acréscimo fica em R${moeda.aumentar_moeda(valor, porcentagem):.2f}')
        while True:
            y = 0
            porcentagem1 = str(input('Digite uma porcentagem que deseja diminuir do valor inserido: ')).replace(',', '.')
            if porcentagem1.isalpha():
                y = -1
            if y == -1:
                print('Valor inválido!')
            if y != -1:
                porcentagem1 = float(porcentagem1)
                break
        print(f'O valor R${valor} com {porcentagem1}% de diminuição fica em R${moeda.diminuir_moeda(valor, porcentagem):.2f}')
        while True:
            r1 = str(input('Deseja continuar? [S/N] '))
            if r1 in 'Ss':
                print('OK!')
                break
            elif r1 in 'Nn':
                break
            else:
                print('Resposta inválida!')
        if r1 in 'Nn':
            break


programa()
while True:
    r = str(input('Quer tentar novamente? [S/N] '))
    if r in 'Nn':
        print('Obrigado! Volte Sempre!')
        break
    elif r in 'Ss':
        programa()
    else:
        print('Resposta inválida')

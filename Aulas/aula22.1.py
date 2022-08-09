from uteis import moeda


def programa():
    while True:
        valor = str(input('Digite o valor da moeda que deseja: R$'))
        if valor.isalpha():
            valor = -1
        valor = float(valor)
        if valor == -1:
            print(moeda.dobro_moeda(valor))
            break
        print(f'O dobro do valor é: R${moeda.dobro_moeda(valor):.2f}')
        print(f'A metade do valor é: R${moeda.metade_moeda(valor):.2f}')
        while True:
            porcentagem = str(input('Digite uma porcentagem que deseja aumentar no valor inserido: '))
            if porcentagem.isnumeric():
                porcentagem = int(porcentagem)
                break
            else:
                print('Valor inválido!')
        print(f'O valor R${valor} com {porcentagem}% de acréscimo fica em R${moeda.aumentar_moeda(valor, porcentagem):.2f}')
        while True:
            porcentagem1 = str(input('Digite uma porcentagem que deseja diminuir do valor inserido: '))
            if porcentagem1.isnumeric():
                porcentagem1 = int(porcentagem1)
                break
            else:
                print('Valor inválido!')
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

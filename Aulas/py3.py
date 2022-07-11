from random import randint
num = ''
while num != 'Q'.lower():
    pc = randint(1, 50)
    num = str(input('Escolha par ou impar [P/I] (digite Q pra sair): '))
    if 'P'.lower() in num:
        print('Voce escolheu par! ')
        if pc % 2 == 0:
            print('Voce ganhou! Eu escolhi {}! '.format(pc))
        else:
            print('Voce perdeu! Eu escolhi {}! '.format(pc))
    elif 'I'.lower() in num:
        print('Voce escolheu impar! ')
        if pc % 2 == 0:
            print('Voce perdeu! Eu escolhi {}! '.format(pc))
        else:
            print('Voce ganhou! Eu escolhi {}! '.format(pc))
print('Obrigado por jogar!')

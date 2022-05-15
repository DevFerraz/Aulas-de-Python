import random
pc = random.choice(['Pedra', 'Papel', 'Tesoura'])
user = str(input('Vamos jogar? Escolha pedra, papel ou tesoura: ')).strip()
if pc == 'Pedra' and user == 'PAPEL'.lower():
    print('Voce venceu! Eu escolhi {}! ' .format(pc))
elif pc == 'Pedra' and user == 'TESOURA'.lower():
    print('Ganhei! Eu escolhi {}! ' .format(pc))
elif pc == 'Pedra' and user == 'PEDRA'.lower():
    print('Empate! eu tambem escolhi {}! ' .format(pc))
elif pc == 'Papel' and user == 'TESOURA'.lower():
    print('Voce venceu! Eu escolhi {}! ' .format(pc))
elif pc == 'Papel' and user == 'PEDRA'.lower():
    print('Ganhei! Eu escolhi {}! ' .format(pc))
elif pc == 'Papel' and user == 'PAPEL'.lower():
    print('Empate! eu tambem escolhi {}! ' .format(pc))
elif pc == 'Tesoura' and user == 'PEDRA'.lower():
    print('Voce venceu! Eu escolhi {}! ' .format(pc))
elif pc == 'Tesoura' and user == 'PAPEL'.lower():
    print('Ganhei! Eu escolhi {}! ' .format(pc))
elif pc == 'Tesoura' and user == 'TESOURA'.lower():
    print('Empate! eu tambem escolhi {}! ' .format(pc))
else:
    print('Opcao invalida! ')
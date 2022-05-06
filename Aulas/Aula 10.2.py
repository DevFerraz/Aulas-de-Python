n = float(input('Digite a velocidade que o veiculo passou: '))
if n > 80:
    print('O veiculo foi multado! A multa eh de: {:.2f}' .format((n-80)*7))
else:
    print('O veiculo passou em velocidade permitida e nao foi multado! ')
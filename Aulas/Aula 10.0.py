n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
n3 = (n1 + n2)/2
print('Sua media eh de {:.1f} pontos!' .format(n3))
if n3 >= 6.0:
    print('Parabens! Voce passou!')
else:
    print('Vish... te aguardo na recuperacao :( ')

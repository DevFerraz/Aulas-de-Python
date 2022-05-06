km = float(input('Digite a distancia da viagem que sera feita: '))
km1 = km * 0.7
km2 = km * 0.55
if km <= 200:
    print('Sua viagem ira custar R${:.2f} ' .format(km1))
else:
    print('Sua viagem ira custar R${:.2f} ' .format(km2))
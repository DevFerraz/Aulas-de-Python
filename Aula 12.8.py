peso = float(input('Digite seu peso (em quilos): '))
altura = float(input('Digite sua altura (em metros): '))
IMC = peso / (altura * altura)
if IMC < 18.5:
    print('Seu IMC eh de {:.1f} e voce esta abaixo do peso! ' .format(IMC))
elif IMC <= 25:
    print('Seu IMC eh de {:.1f} e voce esta no peso ideal! '.format(IMC))
elif IMC <= 30:
    print('Seu IMC eh de {:.1f} e voce esta em sobrepeso! '.format(IMC))
elif IMC <= 40:
    print('Seu IMC eh de {:.1f}. Cuidado, voce esta obeso! '.format(IMC))
elif IMC > 40:
    print('Seu IMC eh de {:.1f} e voce esta em obesidade morbida! Precisamos mudar sua dieta! '.format(IMC))
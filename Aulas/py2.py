c = num = 0
num = int(input('Digite a tabuada que quer ver: '))
while num >= 0:
    for c in range(1, 10):
        print(f'{c} x {num} = {c * num}\n')
    if c > 11:
        break
    num = int(input('Digite a tabuada que quer ver: '))
print('Voce digitou um numero negativo, por isso, o programa foi encerrado.')

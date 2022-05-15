import time
print('Seja bem-vindo a Confederacao Nacional de Natacao!')
time.sleep(1)
idade = int(input('Digite a idade do atleta para saber sua categoria: '))
if idade <= 9:
    print('O atleta esta na categoria mirim! ')
elif idade <= 14:
    print('O atleta esta na categoria infantil! ')
elif idade <= 19:
    print('O atleta esta na categoria junior! ')
elif idade <= 20:
    print('O atleta esta na categoria senior! ')
else:
    print('O atleta esta na categoria master! ')
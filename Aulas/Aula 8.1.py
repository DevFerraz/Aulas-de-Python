import math
cat1 = float(input('Digite o valor do cateto oposto: '))
cat2 = float(input('Digite o valor do cateto adjacente: '))
print('O valor da hipotenusa eh: {}' .format(math.hypot(cat1, cat2)))
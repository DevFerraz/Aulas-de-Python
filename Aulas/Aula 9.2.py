num = int(input('Digite um numero entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('A unidade de milhar eh: {}' .format(m))
print('A unidade de centena eh: {}' .format(c))
print('A unidade de dezena eh: {}' .format(d))
print('A unidade do numero eh: {}' .format(u))
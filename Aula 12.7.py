import time
n1 = float(input('Digite o valor da primeira reta para formar um triangulo: '))
n2 = float(input('Digite o valor da segunda reta: '))
n3 = float(input('Digite o valor da terceira reta: '))
n4 = n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2
if n4 == 1:
    print('Otimo, esses sao valores possiveis para formar um triangulo! ')
else:
    print('Nao eh possivel formar um triangulo! ')
time.sleep(1)
if n1 == n2 == n3 and n4 == 1:
    print('O triangulo formado foi equilatero! ')
elif n1 == n2 or n1 == n3 or n2 == n3 and n4 == 1:
    print('O triangulo formado foi isosceles! ')
elif n1 != n2 != n3 and n4 == 1:
    print('O triangulo formado foi escaleno! ')
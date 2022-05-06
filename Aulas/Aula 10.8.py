n1 = float(input('Digite o valor da primeira reta para formar um triangulo: '))
n2 = float(input('Digite o valor da segunda reta: '))
n3 = float(input('Digite o valor da terceira reta: '))
maior = n1
if n2 > n1 - n3 or n2 > n3 - n1:
    maior = n2
if n2 < n3 + n1:
    maior = n2
if n3 > n1 - n2 or n3 > n2 - n1:
    maior = n3
if n3 < n1 + n2:
    maior = n3
if maior < n1 - n2 or maior < n3 - n2 or maior < n1 - n3:
    print('Nao eh possivel fazer um triangulo com essas medidas! ')
if maior > n1 + n2 or maior > n2 + n3 or maior > n1 + n3:
    print('\033[1;34;40mNao eh possivel fazer um triangulo com essas medidas!\033[m ')
else:
    print('Eh possivel fazer um triangulo com essas medidas! ')

'''Muito mais facil fazer: if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2'''

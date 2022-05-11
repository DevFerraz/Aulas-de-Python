num1 = float(input('Digite um valor qualquer: '))
num2 = float(input('Digite outro valor qualquer: '))
if num1 > num2:
    print('O primeiro valor digitado eh maior que o segundo! ')
elif num1 < num2:
    print('O segundo valor digitado eh maior que o primeiro! ')
elif num1 == num2:
    print('Os valores digitados sao iguais! ')
else:
    print('Voce tem certeza que digitou valores validos? ')
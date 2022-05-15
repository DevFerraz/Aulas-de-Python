try:
    num1 = str(input('Digite um valor qualquer: '))
    num2 = str(input('Digite outro valor qualquer: '))
print('Voce tem certeza que digitou valores validos? ')
except:
if num1 > num2:
    print('O primeiro valor digitado eh maior que o segundo! ')
elif num1 < num2:
    print('O segundo valor digitado eh maior que o primeiro! ')
elif num1 == num2:
    print('Os valores digitados sao iguais! ')

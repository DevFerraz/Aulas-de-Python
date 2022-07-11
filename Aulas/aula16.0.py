extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze')
extenso += ('Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
num = int(input('Digite o número que deseja ver por extenso (1 a 20): '))

for c in range(len(extenso)):
    if c == num:
        print(f'Voce digitou o numero {extenso[num]}')
if num < 0 or num > 20:
    print('Número inválido! ')

# extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze')
# extenso += ('Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
# while True:
#       num = int(input('Digite um numero entre 0 e 20:))
#       if 0 <= num <= 20:
#           break
#       print('Tente novamente. ', end = '')
# print(f'Voce digitou o numero {extenso[num]}')

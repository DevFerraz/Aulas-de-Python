try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com o tipo de dados que você digitou... ')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero! ')
except KeyboardInterrupt:
    print('O usuário não digitou os dados necessários... ')
except Exception as erro:
    print(f'Tivemos um erro {erro.__cause__}')
else:
    print(f'O resultado é: {r:.2f}')
finally:
    print('Muito Obrigado! Volte Sempre! ')

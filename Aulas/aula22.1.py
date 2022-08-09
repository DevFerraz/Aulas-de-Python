from uteis import moeda


valor = float(input('Digite o valor da moeda que deseja: '))
print(f'O dobro do valor é: {moeda.dobro_moeda(valor)}')
print(f'A metade do valor é: {moeda.metade_moeda(valor)}')
porcentagem = int(input('Digite uma porcentagem que deseja aumentar no valor inserido: '))
print(f'O valor {valor} com {porcentagem}% de acréscimo fica em {moeda.aumentar_moeda(valor, porcentagem)}')
porcentagem1 = int(input('Digite uma porcentagem que deseja diminuir do valor inserido: '))
print(f'O valor {valor} com {porcentagem1}% de diminuição fica em {moeda.diminuir_moeda(valor, porcentagem)}')
nome = input('Qual eh o seu nome completo? ').strip()
print('Seu nome todo em maiusculo eh: {}' .format(nome.upper()))
print('Seu nome todo em minusculo eh: {}' .format(nome.lower()))
divide = nome.split()
divide1 = ''.join(divide)
print('A quantidade total de letras do seu nome eh: {}' .format(len(divide1)))
print('A quantidade de letras do seu primeiro nome eh: {}' .format(len(divide[0])))
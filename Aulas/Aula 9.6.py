nome = str(input('Digite seu nome: ')).strip()
nome1 = nome.split()
print('Seu primeiro nome eh: {}' .format(nome1[0]))
print('Seu ultimo nome eh: {} ' .format(nome1[len(nome1)-1]))

nome = str(input('Digite o nome da sua cidade: ')).strip()
nome1 = nome.find('Santo')
if nome1 == 0:
    print('Sua cidade comeca com Santo! ')
else:
    print('Sua cidade nao comeca com Santo! ')

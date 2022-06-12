mediaidades = 0
somaidades = 0
maioridadehomem = 0
nomedomaisvelho = ''
qtdemulheres = 0
for p in range(1, 5):
    print('----- {} pessoa -----' .format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidades += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomedomaisvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomedomaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        qtdemulheres += 1
mediaidades = somaidades / 4
print('A media de idades do grupo eh {:.1f} anos. ' .format(mediaidades))
print('O homem mais velho tem {} anos e se chama {}. ' .format(maioridadehomem, nomedomaisvelho))
print('A quantidade de mulheres do grupo com menos de 20 anos eh igual a {}. ' .format(qtdemulheres))

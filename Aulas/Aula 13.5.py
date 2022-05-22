termo = int(input('Digite o primeiro termo da progressao: '))
razao = int(input('Digite a razao da progressao: '))
termo1 = 1
for c in range(0, 10):
    print('{} com razao {} eh o {} termo da progressao' .format(termo, razao, termo1))
    termo = termo + razao
    termo1 = termo1 + 1
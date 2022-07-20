def area(b, c):
    a = b * c
    print(f'A área do terreno com as medidas {b}m e {c}m é igual a {a:5.2f}m²')


largura = float(input('Digite a largura total do seu terreno: '))
comprimento = float(input('Digite o comprimento total do seu terreno: '))
area(largura, comprimento)


c = 0
s = 0
while True:
    num = int(input('Digite um numero inteiro (999 para sair): '))
    if num == 999:
        break
    c += 1
    s +=num
print(f'A quantidade de valores foi {c} e a soma entre eles vale {s}')
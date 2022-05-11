value = float(input('Qual eh o valor do imovel? '))
income = float(input('Quanto voce recebe? '))
time = float(input('Em quantos anos voce quer parcelar o imovel? '))
time2 = time*12
factor1 = value/time2
if factor1 > income*0.3:
    print('Seu emprestimo foi negado')
else:
    print('Seu emprestimo foi aprovado! ')
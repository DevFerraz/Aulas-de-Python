nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
nota_final = (nota1 + nota2)/2
if nota_final < 5:
    print('O aluno foi reprovado! ')
elif nota_final <= 5:
    print('O aluno esta de recuperacao! ')
else:
    print('O aluno foi aprovado! ')
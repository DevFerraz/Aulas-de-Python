pilha = []
expressao = str(input('Digite sua expressão para saber se é válida ou não: '))
for p in expressao:
    if p == '(':
        pilha.append('(')
    elif p == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é válida! ')
else:
    print('Sua expressão não é válida! ')
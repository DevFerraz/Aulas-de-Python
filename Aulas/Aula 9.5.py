frase = str(input('Digite uma frase: ')).upper().strip()
vezes = frase.count('A')
inicio = frase.find('A'[0])
fim = frase.rfind('A'[0])
print('A letra "A" aparece {} vezes. ' .format(vezes))
print('Ela aparece a primeira vez na posicao {}.' .format(inicio))
print('Ela aparece por ultimo na posicao {}.' .format(fim))
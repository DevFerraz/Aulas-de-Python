def escreva(msg):
    print('-' * len(msg))
    print(f'{msg:^3}')
    print('-' * len(msg))


mensagem = str(input('Digite sua mensagem: '))
escreva(mensagem)

valor_produto = float(input('Digite o valor do produto a ser comprado: '))
forma_pgto = int(input('Digite (1) para pgt em dinheiro ou cheque, (2) para cartao a vista, (3) para cartao em 2x e (4) cartao em 3 ou mais parcelas: '))
if forma_pgto == 1:
    print('Voce escolheu dinheiro/cheque e recebeu 10% de desconto! O valor sera de {:.2f}!' .format(valor_produto*0.9))
elif forma_pgto == 2:
    print('Voce escolheu cartao a vista e recebeu 5% de desconto! O valor sera de {:.2f}' .format(valor_produto*0.95))
elif forma_pgto == 3:
    print('Voce escolheu parcelado em 2x e sua compra nao tera juros! O valor sera de {:.2f}' .format(valor_produto))
elif forma_pgto == 4:
    print('Voce escolheu parcelar de 3x ou mais e sua compra tera 20% de juros. O valor sera de {:.2f}' .format(valor_produto*1.2))
else:
    print('Opcao invalida!')
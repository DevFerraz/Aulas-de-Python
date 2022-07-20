import time


def maior(* num):
    cont = biger = 0
    print('Analisando os valores...')
    for v in num:
        print(v, end=' ')
        time.sleep(1)
        if cont == 0:
            biger = v
        else:
            if v > biger:
                biger = v
        cont += 1
    print()
    print(f'Foram informados {cont} valores.')
    print(f'O maior valor é: {biger}')
    print()


maior(1, 5, 67, 8, 7, 4)
maior(8, 9, 12, 3, 45, -30)
maior(23, 2, 11, 89, 72)




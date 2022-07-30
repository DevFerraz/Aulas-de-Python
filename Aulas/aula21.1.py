def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


r1 = fatorial(5)
r2 = fatorial(6)
r3 = fatorial(7)
print(f'As respostas que eu tive foram: {r1}, {r2} e {r3}. ')

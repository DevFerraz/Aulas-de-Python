def notas(*n, sit=False):
    r = {}
    r['Qtd. Notas'] = len(n)
    r['Maior Nota'] = max(n)
    r['Menor Nota'] = min(n)
    r['Média'] = sum(n)/len(n)
    if sit:
        if 10 < r['Média'] or r['Média'] < 0:
            r['Situação'] = 'Valor de média final inválido. Revise as notas.'
        elif 0 <= r['Média'] < 5:
            r['Situação'] = 'Reprovado'
        elif 5 < r['Média'] < 7:
            r['Situação'] = 'Em recuperação'
        elif r['Média'] > 7:
            r['Situação'] = 'Aprovado'
    return r


resp = notas(3, 4, 6.5, sit=True)
print(resp)

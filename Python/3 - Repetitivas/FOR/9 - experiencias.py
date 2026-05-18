coelhos = ratos = sapos = total = 0
casos_de_teste = int(input('Quantos casos de teste serão digitados? '))
for i in range(0, casos_de_teste):
    quant = int(input('Quantidade de cobaias: '))
    tipo = input('Tipo de cobaia (C/S/R): ').upper()
    total += quant
    if tipo == 'C':
        coelhos += quant
    elif tipo == 'S':
        sapos += quant
    elif tipo == 'R':
        ratos += quant

print('RELATORIO FINAL:')
print(f'Total: {total} cobaias.')
print(f'Total de coelhos: {coelhos}')
print(f'Total de ratos: {ratos}')
print(f'Total de sapos {sapos}')
print(f'Percentual de coelhos: {(coelhos / total) * 100:.2f}')
print(f'Percentual de ratos: {(ratos / total) * 100:.2f}')
print(f'Percentual de sapos: {(sapos / total) * 100:.2f}')

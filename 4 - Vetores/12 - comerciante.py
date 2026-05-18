n = int(input('Serao digitados dados de quantos produtos? '))

nome = [0 for i in range(n + 1)]
precocompra = [0 for i in range(n + 1)]
precovenda = [0 for i in range(n + 1)]
lucro = [0 for i in range(n + 1)]
menordedez = entre = maiorquevinte = somacompra = somavenda = somalucro = 0

for i in range(1, n + 1):
    nome[i] = input('Nome: ')
    precocompra[i] = float(input('Preco de compra: '))
    precovenda[i] = float(input('Preco de venda: '))
    lucro[i] = precovenda[i] - precocompra[i]

# PORCENTAGENS
    dez = (precocompra[i] * 10) / 100
    vinte = (precocompra[i] * 20) / 100

# SE LUCRO FOR MENOR QUE 10
    if lucro[i] < dez:
        menordedez += 1

# SE LUCRO FOR ENTRE 10 E 20
    if lucro[i] >= dez and lucro[i] <= vinte:
        entre += 1

# SE LUCRO FOR MAIOR QUE 20
    if lucro[i] > vinte:
        maiorquevinte += 1

# SOMAS
    somacompra += precocompra[i]
    somavenda += precovenda[i]
    somalucro += lucro[i]

print()

print('RELATORIO:')
print(f'Lucro abaixo de 10%: {menordedez}')
print(f'Lucro entre 10% e 20%: {entre}')
print(f'Lucro acima de 20%: {maiorquevinte}')
print(f'Valor total de compra: {somacompra:.2f}')
print(f'Valor total de venda: {somavenda:.2f}')
print(f'Lucro total: {somalucro:.2f}')

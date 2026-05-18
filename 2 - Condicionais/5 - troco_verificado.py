preco = float(input('Preço unitário do produto: '))
quantidade = int(input('Quantidade comprada: '))
dinheiro = float(input('Dinheiro recebido: '))
troco = dinheiro - quantidade * preco
if troco < 0:
    print(f'DINHEIRO INSUFICIENTE. FALTAM {quantidade * preco - dinheiro} REAIS')
else:
    print(f'TROCO = {troco}')
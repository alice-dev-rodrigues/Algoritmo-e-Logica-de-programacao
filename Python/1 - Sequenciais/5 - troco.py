preco = float(input('Preço unitário do produto: '))
quantidade = int(input('Quantidade comprada: '))
dinheiro = float(input('Dinheiro recebido: '))
print(f'TROCO = {dinheiro - (preco * quantidade)}')

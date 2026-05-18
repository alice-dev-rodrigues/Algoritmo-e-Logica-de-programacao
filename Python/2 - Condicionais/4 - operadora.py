minutos = int(input('Digite a quantidade de minutos: '))
valor = 50
if minutos > 100:
    minutos -= 100
    valor = minutos * 2 + 50
print(f'Valor a pagar: R${valor}')

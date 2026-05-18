codigo = int(input('Codigo do produto comprado: '))
quantidade = int(input('Quantidade comprada: '))
if codigo == 1:
    print(f'Valor a pagar: R${quantidade * 5:.2f}')
elif codigo == 2:
    print(f'Valor a pagar: R${quantidade * 3.5:.2f}')
elif codigo == 3:
    print(f'Valor a pagar: R${quantidade * 4.8:.2f}')
elif codigo == 4:
    print(f'Valor a pagar: R${quantidade * 8.9:.2f}')
else:
    print(f'Valor a pagar: R${quantidade * 7.32:.2f}')

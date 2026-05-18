casos = int(input('Quantos casos voce vai digitar? '))
for i in range(0, casos):
    n = int(input('Entre com o numerador: '))
    d = int(input('Entre com o denominador: '))
    if d == 0:
        print('DIVISAO IMPOSSIVEL')
    else:
        print(f'DIVISAO = {n / d}')
        
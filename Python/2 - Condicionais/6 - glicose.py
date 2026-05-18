medida = float(input('Digite a medida da glicose: '))
if medida <= 100:
    print('Classificação: normal')
elif medida > 100 and medida <= 140:
    print('Classificação: elevado')
else:
    print('Classificação: diabetes')
    